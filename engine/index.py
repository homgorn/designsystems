"""FR-2: скоринг по методике индекса. unknown — явно отдельно от no (честность методологии)."""

from __future__ import annotations

from .corpus import signals


def score(slug: str) -> dict:
    sigs = signals(slug)
    by_key = {s["signal_key"]: s for s in sigs}
    confirmed = sum(1 for s in sigs if s["status"] == "yes")
    return {
        "slug": slug,
        "score": confirmed,  # 0..5 подтверждённых сигналов
        "max": 5,
        "signals": by_key,
        "unknown": [s["signal_key"] for s in sigs if s["status"] == "unknown"],
    }


def top(n: int = 10) -> list[tuple[str, int]]:
    from .corpus import _connect  # локально: внутренний доступ к списку систем
    con = _connect()
    try:
        rows = con.execute(
            "SELECT slug, score FROM ai_ready_systems ORDER BY score DESC, slug LIMIT ?", (n,)).fetchall()
        return [(r[0], r[1]) for r in rows]
    finally:
        con.close()
