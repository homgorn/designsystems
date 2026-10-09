"""FR-9: CLI stats|check|export|audit. JSON-вывод + exit-code != 0 при провале гейта."""

from __future__ import annotations

import argparse
import json
import sys

from .checks import check
from .corpus import counts, search
from .exporters import design_md
from .index import score, top


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(prog="engine")
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("stats")
    p = sub.add_parser("check")
    p.add_argument("url")
    p.add_argument("--repo", default=None)
    p.add_argument("--min-score", type=int, default=0)
    p = sub.add_parser("export")
    p.add_argument("slug")
    p.add_argument("--format", choices=["design-md"], default="design-md")
    p = sub.add_parser("audit")
    p.add_argument("query")
    p.add_argument("--limit", type=int, default=10)
    a = ap.parse_args(argv)
    if a.cmd == "stats":
        print(json.dumps(counts(), indent=2, ensure_ascii=False))
        return 0
    if a.cmd == "check":
        res = check(a.url, a.repo)
        print(json.dumps(res, indent=2, ensure_ascii=False))
        return 0 if res["score"] >= a.min_score else 1
    if a.cmd == "export":
        from .corpus import _connect
        con = _connect()
        try:
            row = con.execute("SELECT payload FROM breakdowns WHERE slug=?", (a.slug,)).fetchone()
        finally:
            con.close()
        if not row:
            print(json.dumps({"error": f"unknown slug: {a.slug}"}))
            return 2
        print(design_md(json.loads(row[0]), a.slug))
        return 0
    if a.cmd == "audit":
        print(json.dumps({"top": top(5), "search": search(a.query, a.limit)},
                         indent=2, ensure_ascii=False))
        return 0
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
