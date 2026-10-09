#!/usr/bin/env python3
"""Query helper for the designsystems.one research corpus.

Usage:
    python scripts/query.py stats            # corpus overview
    python scripts/query.py top [N]          # top-N AI-ready systems
    python scripts/query.py signals          # signal status distribution
    python scripts/query.py system <slug>    # one system: breakdown + signals
    python scripts/query.py search <terms>   # FTS over breakdowns/signals/glossary
    python scripts/query.py glossary [term]  # glossary lookup / dump
    python scripts/query.py money            # monetisation surfaces
    python scripts/query.py sections         # site inventory by section
    python scripts/query.py links <slug>     # outbound links of one breakdown
"""

from __future__ import annotations

import json
import sqlite3
import sys
from pathlib import Path

DB = Path(__file__).resolve().parent.parent / "db" / "designsystems.db"


def q(sql: str, args: tuple = ()):
    con = sqlite3.connect(DB)
    try:
        return con.execute(sql, args).fetchall()
    finally:
        con.close()


def stats() -> None:
    print("corpus_fts rows:", q("SELECT COUNT(*) FROM corpus_fts")[0][0])
    for t in ["design_systems", "breakdowns", "ai_ready_systems",
              "ai_ready_signals", "breakdown_links", "glossary",
              "mcp_tools", "site_urls", "gallery_only", "monetization_surfaces"]:
        print(f"{t:24}{q(f'SELECT COUNT(*) FROM {t}')[0][0]}")


def top(n: int = 12) -> None:
    for name, company, score in q(
        "SELECT name,company,score FROM ai_ready_systems "
        "ORDER BY score DESC, name LIMIT ?", (n,)):
        print(f"{score}/5  {name} ({company})")


def signals() -> None:
    for key, status, cnt in q(
        "SELECT signal_key,status,COUNT(*) FROM ai_ready_signals "
        "GROUP BY 1,2 ORDER BY 1,2"):
        print(f"{key:12}{status:8}{cnt}")


def system(slug: str) -> None:
    row = q("SELECT name,company,url,tagline FROM design_systems WHERE slug=?", (slug,))
    if not row:
        print("unknown slug"); return
    print(f"{row[0][0]} — {row[0][1]}\n{row[0][2]}\n{row[0][3]}\n")
    payload = q("SELECT payload FROM breakdowns WHERE slug=?", (slug,))
    if payload:
        doc = json.loads(payload[0][0])
        keys = [k for k in doc.keys() if not k.startswith("$")]
        print("breakdown keys:", ", ".join(keys[:25]))
        for k in ("origin", "governance", "knownFor", "watchOuts", "evaluation",
                  "anchorComponents", "tokenSnapshot"):
            if k in doc:
                val = doc[k]
                txt = json.dumps(val, ensure_ascii=False)[:1200]
                print(f"\n## {k}\n{txt}")
    print("\n-- AI signals --")
    for key, status, ev in q(
        "SELECT signal_key,status,evidence FROM ai_ready_signals WHERE slug=?", (slug,)):
        print(f"[{status or '?':8}] {key}: {(ev or '')[:160]}")


def search(terms: str, limit: int = 15) -> None:
    rows = q(
        "SELECT entity, entity_id, title FROM corpus_fts "
        "WHERE corpus_fts MATCH ? LIMIT ?", (terms, limit))
    for entity, eid, title in rows:
        print(f"{entity:14}{eid:40}{title}")


def glossary(term: str = "") -> None:
    if term:
        rows = q("SELECT term,definition FROM glossary WHERE term LIKE ?",
                 (f"%{term}%",))
    else:
        rows = q("SELECT term,definition FROM glossary ORDER BY term")
    for t, d in rows:
        print(f"### {t}\n{(d or '')[:400]}\n")


def money() -> None:
    for path, title, kind, note in q(
        "SELECT path,title,kind,note FROM monetization_surfaces ORDER BY kind,path"):
        print(f"[{kind:12}] {path}\n  {title} — {note}\n")


def sections() -> None:
    for section, cnt in q(
        "SELECT section,COUNT(*) FROM site_urls GROUP BY 1 ORDER BY 2 DESC"):
        print(f"{cnt:4}  {section}")


def links(slug: str) -> None:
    for kind, label, url in q(
        "SELECT kind,label,url FROM breakdown_links WHERE slug=? ORDER BY kind",
        (slug,)):
        print(f"[{kind:6}] {label or '-'} -> {url}")


CMDS = {"stats": stats, "top": top, "signals": signals, "system": system,
        "search": search, "glossary": glossary, "money": money,
        "sections": sections, "links": links}


def main(argv: list[str]) -> int:
    if len(argv) < 2 or argv[1] not in CMDS:
        print(__doc__)
        return 1
    fn = CMDS[argv[1]]
    if argv[1] == "top":
        fn(int(argv[2]) if len(argv) > 2 else 12)
    elif argv[1] in ("system", "links"):
        if len(argv) < 3:
            print(f"usage: query.py {argv[1]} <slug>"); return 1
        fn(argv[2])
    elif argv[1] == "search":
        if len(argv) < 3:
            print("usage: query.py search <terms>"); return 1
        fn(" ".join(argv[2:]))
    elif argv[1] == "glossary":
        fn(argv[2] if len(argv) > 2 else "")
    else:
        fn()
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
