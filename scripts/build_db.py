#!/usr/bin/env python3
"""
designsystems.one — research database builder.

Pulls every machine-readable artifact designsystems.one exposes (public APIs,
llms.txt, shadcn registry, MCP discovery doc) into a normalised SQLite database
plus a set of markdown extracts, so downstream agents can query the corpus
without re-hitting the network.

Usage:
    python scripts/build_db.py [--refresh] [--skip-breakdowns]

Outputs:
    db/designsystems.db          normalised SQLite corpus
    research/raw/*.json          verbatim API payloads (cached)
    research/raw/breakdowns/*.json  per-system editorial breakdowns
"""

from __future__ import annotations

import argparse
import json
import re
import sqlite3
import sys
import time
import urllib.error
import urllib.request
from datetime import UTC, datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "research" / "raw"
BREAKDOWNS = RAW / "breakdowns"
DB_PATH = ROOT / "db" / "designsystems.db"

BASE = "https://www.designsystems.one"
UA = "Mozilla/5.0 (compatible; designsystems-research/1.0)"

ENDPOINTS = {
    "api_design_systems": "api-design-systems.json",
    "api_ai_ready": "api-ai-ready.json",
    "api_ai_ready_csv": "api-ai-ready.csv",
    "api_glossary": "api-glossary.json",
    "api_mcp": "mcp-discovery.json",
    "registry": "registry-index.json",
    "llms_txt": "llms.txt",
    "llms_full_txt": "llms-full.txt",
    "sitemap": "sitemap.xml",
    "robots": "robots.txt",
}

ENDPOINT_URLS = {k: f"{BASE}{v}" for k, v in {
    "api_design_systems": "/api/design-systems",
    "api_ai_ready": "/api/ai-ready/systems",
    "api_ai_ready_csv": "/api/ai-ready/systems.csv",
    "api_glossary": "/api/glossary",
    "api_mcp": "/api/mcp",
    "registry": "/r",
    "llms_txt": "/llms.txt",
    "llms_full_txt": "/llms-full.txt",
    "sitemap": "/sitemap.xml",
    "robots": "/robots.txt",
}.items()}

# pre-seeded filenames captured by earlier manual crawls
LEGACY_NAMES = {
    "api_design_systems": "api-design-systems.json",
    "api_ai_ready": "api-ai-ready.json",
    "api_glossary": "api-glossary.json",
    "api_mcp": "mcp-discovery.json",
    "registry": "registry-index.json",
}

SCHEMA = """
PRAGMA journal_mode=WAL;
PRAGMA foreign_keys=ON;

-- ---------- source metadata ----------
CREATE TABLE IF NOT EXISTS crawl_meta (
    key         TEXT PRIMARY KEY,
    value       TEXT,
    fetched_at  TEXT
);

CREATE TABLE IF NOT EXISTS source_files (
    name        TEXT PRIMARY KEY,
    url         TEXT,
    path        TEXT,
    bytes       INTEGER,
    content_sha TEXT,
    fetched_at  TEXT
);

-- ---------- gallery ----------
CREATE TABLE IF NOT EXISTS design_systems (
    slug           TEXT PRIMARY KEY,
    name           TEXT,
    company        TEXT,
    url            TEXT,
    tagline        TEXT,
    breakdown_url  TEXT,
    rich_breakdown INTEGER DEFAULT 0,
    in_gallery     INTEGER DEFAULT 0,   -- present in /design-systems HTML slug list
    first_seen     TEXT
);

CREATE TABLE IF NOT EXISTS gallery_only (
    -- slugs that appear in the gallery but carry no rich breakdown entry
    slug        TEXT PRIMARY KEY,
    resolved_url TEXT,
    note        TEXT
);

-- ---------- editorial breakdowns ----------
CREATE TABLE IF NOT EXISTS breakdowns (
    slug        TEXT PRIMARY KEY REFERENCES design_systems(slug),
    payload     TEXT NOT NULL,       -- verbatim JSON
    fetched_at  TEXT,
    FOREIGN KEY (slug) REFERENCES design_systems(slug)
);

CREATE TABLE IF NOT EXISTS breakdown_links (
    id        INTEGER PRIMARY KEY,
    slug      TEXT NOT NULL REFERENCES breakdowns(slug),
    kind      TEXT,                 -- docs / repo / figma / npm / social ...
    label     TEXT,
    url       TEXT
);
CREATE INDEX IF NOT EXISTS idx_bd_links_slug ON breakdown_links(slug);

-- ---------- agent-ready index ----------
CREATE TABLE IF NOT EXISTS ai_ready_systems (
    slug          TEXT PRIMARY KEY,
    name          TEXT,
    company       TEXT,
    breakdown_url TEXT,
    score         INTEGER,           -- 0..5 confirmed signals
    checked_at    TEXT,
    notes         TEXT
);

CREATE TABLE IF NOT EXISTS ai_ready_signals (
    id            INTEGER PRIMARY KEY,
    slug          TEXT NOT NULL REFERENCES ai_ready_systems(slug),
    signal_key    TEXT NOT NULL,     -- mcp | llmsTxt | dtcg | registry | codeConnect
    signal_label  TEXT,
    status        TEXT,              -- yes | no | unknown | n/a
    note          TEXT,
    evidence      TEXT,
    source_url    TEXT,
    method        TEXT,
    version       TEXT,
    verification  TEXT,
    UNIQUE (slug, signal_key)
);
CREATE INDEX IF NOT EXISTS idx_sig_slug ON ai_ready_signals(slug);
CREATE INDEX IF NOT EXISTS idx_sig_status ON ai_ready_signals(status);

-- ---------- glossary ----------
CREATE TABLE IF NOT EXISTS glossary (
    term       TEXT PRIMARY KEY,
    definition TEXT,
    payload    TEXT
);

-- ---------- shadcn registry ----------
CREATE TABLE IF NOT EXISTS registry_items (
    name                 TEXT PRIMARY KEY,
    type                 TEXT,
    description          TEXT,
    url                  TEXT,
    dependencies         TEXT,   -- JSON array
    registry_dependencies TEXT
);

-- ---------- MCP surface ----------
CREATE TABLE IF NOT EXISTS mcp_server (
    id            INTEGER PRIMARY KEY CHECK (id = 1),
    name          TEXT,
    version       TEXT,
    protocol      TEXT,
    transport     TEXT,
    endpoint      TEXT,
    alias         TEXT,
    docs          TEXT,
    auth          TEXT,
    payload       TEXT,
    fetched_at    TEXT
);

CREATE TABLE IF NOT EXISTS mcp_tools (
    name       TEXT PRIMARY KEY,
    ord        INTEGER
);

CREATE TABLE IF NOT EXISTS mcp_prompts (
    name       TEXT PRIMARY KEY
);

CREATE TABLE IF NOT EXISTS mcp_resources (
    uri        TEXT PRIMARY KEY
);

-- ---------- products / monetisation surfaces ----------
CREATE TABLE IF NOT EXISTS monetization_surfaces (
    id        INTEGER PRIMARY KEY,
    path      TEXT UNIQUE,
    title     TEXT,
    kind      TEXT,          -- paid-product | donation | tool | api | registry
    note      TEXT,
    source    TEXT
);

-- ---------- site inventory ----------
CREATE TABLE IF NOT EXISTS site_urls (
    url         TEXT PRIMARY KEY,
    lastmod     TEXT,
    changefreq  TEXT,
    priority    TEXT,
    section     TEXT
);
CREATE INDEX IF NOT EXISTS idx_site_section ON site_urls(section);

-- ---------- research notes from agents ----------
CREATE TABLE IF NOT EXISTS research_docs (
    id        INTEGER PRIMARY KEY,
    topic     TEXT UNIQUE,
    path      TEXT,
    words     INTEGER,
    summary   TEXT,
    added_at  TEXT
);

-- ---------- FTS ----------
CREATE VIRTUAL TABLE IF NOT EXISTS corpus_fts USING fts5(
    entity, entity_id, title, body,
    tokenize = 'porter unicode61'
);
"""


# --------------------------------------------------------------------------- net
def fetch(url: str, tries: int = 3, timeout: int = 60) -> bytes:
    last: Exception | None = None
    for attempt in range(1, tries + 1):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                return resp.read()
        except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError) as exc:
            last = exc
            if attempt < tries:
                time.sleep(1.5 * attempt)
    raise RuntimeError(f"failed to fetch {url}: {last}")


def fetch_cached(name: str, url: str, refresh: bool) -> bytes:
    RAW.mkdir(parents=True, exist_ok=True)
    path = RAW / name
    if path.exists() and not refresh:
        return path.read_bytes()
    data = fetch(url)
    path.write_bytes(data)
    print(f"  [net] {name}  {len(data):,}b")
    return data


def sha256(data: bytes) -> str:
    import hashlib

    return hashlib.sha256(data).hexdigest()


def now() -> str:
    return datetime.now(UTC).isoformat(timespec="seconds")


def jload(data: bytes):
    # utf-8-sig tolerates a BOM from PowerShell's `-Encoding utf8` output
    return json.loads(data.decode("utf-8-sig", errors="replace"))


# --------------------------------------------------------------------------- helpers
def as_list(value) -> list:
    if value is None:
        return []
    if isinstance(value, list):
        return value
    return [value]


def dump(value) -> str:
    return json.dumps(value, ensure_ascii=False)


def deep_find_links(obj, base: str = "") -> list[tuple[str, str, str]]:
    """Walk an arbitrary JSON payload and yield (kind, label, url) for every
    http(s) string. Classifies by host/pattern so the breakdown links table is
    queryable without knowing the payload's exact shape."""
    found: list[tuple[str, str, str]] = []

    def classify(url: str, key_hint: str = "") -> str:
        u = url.lower()
        if "github.com" in u:
            return "repo"
        if "figma.com" in u:
            return "figma"
        if "npmjs.com" in u or "npm." in u:
            return "npm"
        if "designsystem" in u or "design-system" in u or "design.md" in u:
            return "docs"
        if "linkedin.com" in u or "twitter.com" in u or "x.com" in u:
            return "social"
        if "blog" in u or "medium.com" in u:
            return "blog"
        if u.endswith(".pdf"):
            return "pdf"
        return key_hint or "other"

    def walk(node, hint=""):
        if isinstance(node, dict):
            for k, v in node.items():
                walk(v, str(k))
        elif isinstance(node, list):
            for v in node:
                walk(v, hint)
        elif isinstance(node, str) and node.startswith(("http://", "https://")):
            found.append((classify(node, hint), hint, node))

    walk(obj)
    # de-dupe, keep first classification
    seen: dict[str, str] = {}
    for kind, hint, url in found:
        seen.setdefault(url, f"{kind}|{hint}")
    return [(meta.split("|")[0], meta.split("|")[1], u) for u, meta in seen.items()]


# --------------------------------------------------------------------------- build
def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--refresh", action="store_true", help="ignore cache, re-fetch")
    ap.add_argument("--skip-breakdowns", action="store_true")
    args = ap.parse_args()

    RAW.mkdir(parents=True, exist_ok=True)
    BREAKDOWNS.mkdir(parents=True, exist_ok=True)
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)

    # adopt any already-downloaded files from the manual first pass
    for key, legacy in LEGACY_NAMES.items():
        src, dst = RAW / legacy, RAW / ENDPOINTS[key]
        if src.exists() and src != dst and not dst.exists():
            src.replace(dst)

    con = sqlite3.connect(DB_PATH)
    con.executescript(SCHEMA)
    cur = con.cursor()
    stamp = now()

    # ---------------- 1. raw source files ----------------
    print("[1/8] source artifacts")
    payloads: dict[str, object] = {}
    for key, name in ENDPOINTS.items():
        url = ENDPOINT_URLS[key]
        data = fetch_cached(name, url, args.refresh)
        cur.execute(
            "INSERT OR REPLACE INTO source_files VALUES (?,?,?,?,?,?)",
            (name, url, str(RAW / name), len(data), sha256(data), stamp),
        )
        if name.endswith(".json"):
            payloads[key] = jload(data)

    # ---------------- 2. gallery ----------------
    print("[2/8] gallery")
    # slugs scraped from the rendered gallery HTML
    html_path = RAW / "design-systems.html"
    gallery_slugs: set[str] = set()
    if html_path.exists():
        html = html_path.read_text(encoding="utf-8", errors="replace")
        gallery_slugs = set(re.findall(r"/design-systems/([a-z0-9\-]+)", html))
        print(f"      gallery slugs in HTML: {len(gallery_slugs)}")

    api_ds = payloads["api_design_systems"]
    items = api_ds.get("items", api_ds if isinstance(api_ds, list) else [])
    for it in items:
        slug = it.get("slug")
        if not slug:
            continue
        cur.execute(
            "INSERT OR REPLACE INTO design_systems "
            "(slug,name,company,url,tagline,breakdown_url,rich_breakdown,in_gallery,first_seen) "
            "VALUES (?,?,?,?,?,?,?,?,?)",
            (
                slug,
                it.get("name"),
                it.get("company"),
                it.get("url"),
                it.get("tagline"),
                it.get("breakdownUrl"),
                1 if it.get("richBreakdown") else 0,
                1 if slug in gallery_slugs else 0,
                stamp,
            ),
        )
        cur.execute(
            "INSERT INTO corpus_fts(entity,entity_id,title,body) VALUES('design_system',?,?,?)",
            (slug, it.get("name"), " ".join(filter(None, [it.get("company"), it.get("tagline")]))),
        )
    print(f"      rich breakdowns: {len(items)}")

    # gallery-only slugs (category/tooling pages surfaced by the regex)
    known = {it.get("slug") for it in items}
    for slug in sorted(gallery_slugs - known):
        cur.execute(
            "INSERT OR REPLACE INTO gallery_only(slug,resolved_url,note) VALUES (?,?,?)",
            (slug, f"{BASE}/design-systems/{slug}", "linked from gallery; not in /api/design-systems"),
        )
    if gallery_slugs - known:
        print(f"      gallery-only (non-breakdown) pages: {len(gallery_slugs - known)}")

    # ---------------- 3. breakdowns ----------------
    if not args.skip_breakdowns:
        print(f"[3/8] breakdowns ({len(items)} systems)")
        for n, it in enumerate(items, 1):
            slug = it.get("slug")
            if not slug:
                continue
            url = f"{BASE}/api/design-systems/{slug}"
            try:
                data = fetch_cached(f"breakdowns/{slug}.json", url, args.refresh)
                doc = jload(data)
            except (OSError, ValueError, RuntimeError, KeyError) as exc:  # keep going; partial corpus is still useful
                print(f"      !! {slug}: {exc}")
                continue
            cur.execute(
                "INSERT OR REPLACE INTO breakdowns(slug,payload,fetched_at) VALUES (?,?,?)",
                (slug, data.decode("utf-8", errors="replace"), stamp),
            )
            cur.execute("DELETE FROM breakdown_links WHERE slug = ?", (slug,))
            for kind, label, lurl in deep_find_links(doc, base=slug):
                cur.execute(
                    "INSERT INTO breakdown_links(slug,kind,label,url) VALUES (?,?,?,?)",
                    (slug, kind, label, lurl),
                )
            name = (doc.get("name") if isinstance(doc, dict) else None) or it.get("name")
            tagline = (doc.get("tagline") if isinstance(doc, dict) else None) or it.get("tagline")
            cur.execute(
                "INSERT INTO corpus_fts(entity,entity_id,title,body) VALUES('breakdown',?,?,?)",
                (slug, name, f"{tagline} {json.dumps(doc, ensure_ascii=False)[:20000]}"),
            )
            if n % 10 == 0:
                print(f"      {n}/{len(items)}")
    else:
        print("[3/8] breakdowns — skipped")

    # ---------------- 4. agent-ready index ----------------
    print("[4/8] agent-ready index")
    ar = payloads["api_ai_ready"]
    systems = ar.get("items") or ar.get("systems") or (ar if isinstance(ar, list) else [])
    for sysdoc in systems:
        slug = sysdoc.get("slug")
        if not slug:
            continue
        ev = sysdoc.get("evidence") or {}
        cur.execute(
            "INSERT OR REPLACE INTO ai_ready_systems VALUES (?,?,?,?,?,?,?)",
            (
                slug,
                sysdoc.get("name"),
                sysdoc.get("company"),
                sysdoc.get("breakdownUrl"),
                sysdoc.get("score"),
                ev.get("checkedAt"),
                sysdoc.get("notes") or ev.get("notes"),
            ),
        )
        signals = sysdoc.get("signals") or {}
        for key, val in signals.items():
            val = val or {}
            detail = {}
            for sig in ev.get("signals", []) or []:
                if sig.get("key") == key:
                    detail = sig
                    break
            cur.execute(
                "INSERT OR REPLACE INTO ai_ready_signals "
                "(slug,signal_key,signal_label,status,note,evidence,source_url,method,version,verification) "
                "VALUES (?,?,?,?,?,?,?,?,?,?)",
                (
                    slug,
                    key,
                    detail.get("label"),
                    val.get("status"),
                    detail.get("note"),
                    val.get("evidence"),
                    detail.get("source"),
                    detail.get("method"),
                    detail.get("version"),
                    detail.get("verification"),
                ),
            )
            cur.execute(
                "INSERT INTO corpus_fts(entity,entity_id,title,body) VALUES('ai_signal',?,?,?)",
                (f"{slug}:{key}", f"{sysdoc.get('name')} — {detail.get('label')}",
                 " ".join(filter(None, [val.get("status"), val.get("evidence"), detail.get("note")]))),
            )
        coverage = ev.get("coverage") or {}
        if coverage:
            cur.execute(
                "INSERT INTO crawl_meta VALUES (?,?,?) "
                "ON CONFLICT(key) DO UPDATE SET value=excluded.value, fetched_at=excluded.fetched_at",
                (f"coverage:{slug}", dump(coverage), stamp),
            )
    print(f"      systems audited: {len(systems)}")

    # ---------------- 5. glossary ----------------
    print("[5/8] glossary")
    gl = payloads["api_glossary"]
    terms = gl.get("items", gl.get("terms", gl if isinstance(gl, list) else []))
    for t in terms:
        term = t.get("term") or t.get("name")
        if not term:
            continue
        definition = t.get("definition") or t.get("plain") or t.get("text")
        cur.execute("INSERT OR REPLACE INTO glossary VALUES (?,?,?)", (term, definition, dump(t)))
        cur.execute(
            "INSERT INTO corpus_fts(entity,entity_id,title,body) VALUES('glossary',?,?,?)",
            (term, term, definition or ""),
        )
    print(f"      terms: {len(terms)}")

    # ---------------- 6. registry + MCP ----------------
    print("[6/8] registry + MCP")
    reg = payloads["registry"]
    for it in reg.get("items", []):
        cur.execute(
            "INSERT OR REPLACE INTO registry_items VALUES (?,?,?,?,?,?)",
            (
                it.get("name"),
                it.get("type"),
                it.get("description"),
                it.get("url"),
                dump(it.get("dependencies")),
                dump(it.get("registryDependencies")),
            ),
        )
    mcp = payloads["api_mcp"]
    srv = mcp.get("server", {})
    cur.execute(
        "INSERT OR REPLACE INTO mcp_server VALUES (1,?,?,?,?,?,?,?,?,?,?)",
        (
            srv.get("name"), srv.get("version"), srv.get("protocol"), mcp.get("transport"),
            mcp.get("endpoint"), mcp.get("alias"), mcp.get("docs"), mcp.get("auth"),
            dump(mcp), stamp,
        ),
    )
    for n, t in enumerate(mcp.get("tools", []) or []):
        cur.execute("INSERT OR REPLACE INTO mcp_tools VALUES (?,?)", (t, n))
    for p in mcp.get("prompts", []) or []:
        cur.execute("INSERT OR REPLACE INTO mcp_prompts VALUES (?)", (p,))
    for r in mcp.get("resources", []) or []:
        cur.execute("INSERT OR REPLACE INTO mcp_resources VALUES (?)", (r,))
    print(f"      registry items: {len(reg.get('items', []))}  mcp tools: {len(mcp.get('tools', []))}")

    # ---------------- 7. sitemap + monetisation ----------------
    print("[7/8] site inventory + monetisation surfaces")
    xml = (RAW / "sitemap.xml").read_text(encoding="utf-8", errors="replace")
    for block in re.findall(r"<url>(.*?)</url>", xml, re.DOTALL):
        loc = re.search(r"<loc>(.*?)</loc>", block)
        if not loc:
            continue
        url = loc.group(1).strip()
        lm = re.search(r"<lastmod>(.*?)</lastmod>", block)
        cf = re.search(r"<changefreq>(.*?)</changefreq>", block)
        pr = re.search(r"<priority>(.*?)</priority>", block)
        path = url.replace(BASE, "") or "/"
        section = (
            path.strip("/").split("/")[0] if path != "/" else "home"
        )
        cur.execute(
            "INSERT OR REPLACE INTO site_urls VALUES (?,?,?,?,?)",
            (url, lm.group(1) if lm else None, cf.group(1) if cf else None,
             pr.group(1) if pr else None, section),
        )

    surfaces = [
        ("/products/agent-ready-starter/walkthrough", "Agent-Ready Starter (walkthrough)", "paid-product",
         "Only commercial page in the sitemap; a walkthrough for a starter kit."),
        ("/products/agent-ready-starter", "Agent-Ready Starter", "paid-product",
         "Landing for the starter product; walkthrough route is in the sitemap."),
        ("/tools/token-generator", "Token Generator", "tool", "11 export formats, APCA+WCAG dual scoring."),
        ("/tools/accessibility-checklist", "Accessibility Checklist", "tool", "WCAG 2.1 audit + in-page contrast tester."),
        ("/tools/grid-builder", "Grid Builder", "tool", "Responsive grid composer."),
        ("/tools/roi-calculator", "ROI Calculator", "tool", "Quantifies DS adoption gains."),
        ("/tools/token-diff", "Token Diff", "tool", "Diff two token kits."),
        ("/tools/release-checker", "Release Checker", "tool", "SemVer + breaking-change validation."),
        ("/api/tokens", "Token Generator API", "api", "Programmatic token generation, 11 formats."),
        ("/api/design-systems", "Design Systems API", "api", "JSON index + per-system breakdowns."),
        ("/api/ai-ready/systems", "Agent-Ready Index API", "api", "37 systems x 5 signals, CC BY 4.0."),
        ("/api/glossary", "Glossary API", "api", "Plain-language term list."),
        ("/api/mcp", "MCP Server", "api", "22 tools, 3 prompts, 5 resources, no auth."),
        ("/r", "shadcn Registry", "registry", "npx shadcn@latest add https://www.designsystems.one/r/{name}"),
        ("/dashboard", "Dashboard", "app", "robots.txt disallows; app surface exists."),
        ("/admin", "Admin", "app", "robots.txt disallows; back-office surface exists."),
        ("/buymeacoffee", "Support the project (Buy Me a Coffee)", "donation",
         "https://www.buymeacoffee.com/kzhukouski linked in footer as 'Support the project'."),
    ]
    for path, title, kind, note in surfaces:
        cur.execute(
            "INSERT OR REPLACE INTO monetization_surfaces VALUES (NULL,?,?,?,?,?)",
            (path, title, kind, note, "sitemap + llms.txt + robots.txt, crawled 2026-10-06"),
        )

    cur.execute(
        "INSERT OR REPLACE INTO crawl_meta VALUES (?,?,?)",
        ("last_full_build", stamp, stamp),
    )

    # ---------------- 8. report ----------------
    print("[8/8] done")
    con.commit()
    tables = [
        r[0] for r in cur.execute(
            "SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'corpus_fts%'"
        ).fetchall()
    ]
    print("\n  table                 rows")
    print("  " + "-" * 34)
    for t in sorted(tables):
        n = cur.execute(f"SELECT COUNT(*) FROM {t}").fetchone()[0]
        if n:
            print(f"  {t:<22}{n:>8}")
    con.close()
    print(f"\n  db -> {DB_PATH}  ({DB_PATH.stat().st_size:,} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
