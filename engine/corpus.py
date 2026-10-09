"""FR-1: чтение корпуса SQLite (+FTS). Ошибки — DS-E1xx с hint (EC-1/EC-5)."""

from __future__ import annotations

import sqlite3

from . import SCHEMA_VERSION
from .config import db_path


class CorpusError(Exception):
    def __init__(self, code: str, msg: str, hint: str = ""):
        super().__init__(f"{code}: {msg}" + (f" Hint: {hint}" if hint else ""))
        self.code = code


def _connect() -> sqlite3.Connection:
    db = db_path()
    if not db.exists():
        raise CorpusError(
            "DS-E101",
            f"БД не найдена: {db}",
            "python scripts/build_db.py (см. research/04-fetch-log.md)",
        )
    con = sqlite3.connect(db)
    con.row_factory = sqlite3.Row
    return con


TABLES = (
    "design_systems",
    "breakdowns",
    "ai_ready_systems",
    "ai_ready_signals",
    "breakdown_links",
    "glossary",
    "mcp_tools",
    "site_urls",
    "gallery_only",
    "monetization_surfaces",
    "corpus_fts",
)


def counts() -> dict[str, int]:
    con = _connect()
    try:
        return {t: con.execute(f"SELECT COUNT(*) FROM {t}").fetchone()[0] for t in TABLES}
    finally:
        con.close()


def signals(slug: str) -> list[dict]:
    con = _connect()
    try:
        rows = con.execute(
            "SELECT signal_key, status, evidence, source_url FROM ai_ready_signals WHERE slug=?",
            (slug,),
        ).fetchall()
        if not rows:
            raise CorpusError("DS-E102", f"unknown slug: {slug}", "python scripts/query.py top")
        return [dict(r) for r in rows]
    finally:
        con.close()


def search(query: str, limit: int = 15) -> list[dict]:
    con = _connect()
    try:
        rows = con.execute(
            "SELECT entity, entity_id, title FROM corpus_fts WHERE corpus_fts MATCH ? LIMIT ?",
            (query, limit),
        ).fetchall()
        return [dict(r) for r in rows]
    finally:
        con.close()


def schema_version() -> int:
    con = _connect()
    try:
        row = con.execute("SELECT value FROM crawl_meta WHERE key='schema_version'").fetchone()
        return int(row[0]) if row else 0
    except sqlite3.Error:
        return 0  # legacy БД без версионирования (EC-5: апгрейд в Chunk 0)
    finally:
        con.close()


assert SCHEMA_VERSION >= 1
