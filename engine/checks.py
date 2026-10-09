"""FR-3: раннер проверок {url, repo?} -> {score, checks, evidence}. EC-2/EC-3: кэш/фолбэк, не traceback."""

from __future__ import annotations

import time
import urllib.request
from datetime import UTC, datetime

UA = "designsystems-engine/0.1"
TIMEOUT = 12


def _probe(url: str) -> tuple[bool, str]:
    try:
        req = urllib.request.Request(url, headers={"User-Agent": UA}, method="HEAD")
        with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
            return r.status < 400, f"HTTP {r.status}"
    except (OSError, ValueError) as exc:  # сеть недоступна -> EC-2: фиксируем, не падаем
        return False, f"unreachable: {exc}"


def check(url: str, repo: str | None = None) -> dict:
    t0 = time.time()
    base = url.rstrip("/")
    probes = {
        "llmsTxt": [f"{base}/llms.txt", f"{base}/llms-full.txt"],
        "registry": [f"{base}/r", f"{base}/r/registry.json"],
        "mcp": [f"{base}/api/mcp", f"{base}/mcp"],
    }
    checks, confirmed = [], 0
    for signal, candidates in probes.items():
        ok, ev = False, ""
        for c in candidates:
            ok, ev = _probe(c)
            if ok:
                ev = f"{c} ({ev})"
                break
        else:
            ev = f"not found ({ev})"  # ev хранит последнюю причину пробы, напр. unreachable
        checks.append(
            {
                "signal": signal,
                "status": "yes" if ok else "no",
                "evidence": ev,
                "source_url": candidates[0],
            }
        )
        confirmed += ok
    for signal in ("dtcg", "codeConnect"):
        # без repo доказать отсутствие нельзя -> unknown (методика, FR-3); repo-аудит — P1-модуль
        checks.append(
            {
                "signal": signal,
                "status": "unknown",
                "evidence": "repo audit: see P1" if repo else "needs repo tree read (P1 module)",
                "source_url": None,
            }
        )
    return {
        "url": url,
        "score": confirmed,
        "max": 5,
        "checks": checks,
        "duration_ms": int((time.time() - t0) * 1000),
        "checked_at": datetime.now(UTC).isoformat(timespec="seconds"),
        "cached": False,
    }
