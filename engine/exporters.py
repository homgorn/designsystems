"""FR-4/5/6/10: экспорты. Каждый — с атрибуцией CC BY + checked_at (FR-10)."""

from __future__ import annotations

from datetime import UTC, datetime

ATTRIBUTION = "DesignSystems.one (2026). Agent-Ready Design Systems Index. https://www.designsystems.one/ai-ready/systems"


def _stamp() -> str:
    return datetime.now(UTC).isoformat(timespec="seconds")


def design_md(breakdown: dict, slug: str) -> str:
    """FR-4: DESIGN.md из разбора (токены, типографика, спейсинг, компоненты + evidence)."""
    lines = [
        f"# DESIGN.md — {breakdown.get('name', slug)}",
        "",
        f"Company: {breakdown.get('company', '?')}",
        f"Source: {breakdown.get('url', '')}",
        "",
    ]
    for key in (
        "tokens",
        "typography",
        "spacing",
        "anchorComponents",
        "patterns",
        "origin",
        "governance",
        "knownFor",
        "watchOuts",
    ):
        if breakdown.get(key):
            lines += [f"## {key}", str(breakdown[key])[:2000], ""]
    lines += [f"_Checked at {_stamp()}_", f"_Attribution: {ATTRIBUTION}_"]
    return "\n".join(lines)


def acr_draft(product: str, findings: list[dict], edition: str = "WCAG") -> dict:
    """FR-5: draft ACR. conformance решает ревьюер -> уровни пустые; coverage statement обязателен."""
    criteria = []
    for f in findings:
        criteria.append(
            {
                "criterion": f.get("criterion"),
                "auto": f.get("auto", False),
                "finding": f.get("finding"),
                "evidence": f.get("evidence"),
                "question": None if f.get("auto") else f.get("question", "Verify manually."),
                "conformance": None,
            }
        )  # MUST оставаться пустым до ревьюера
    auto_n = sum(1 for c in criteria if c["auto"])
    return {
        "product": product,
        "edition": edition,
        "coverage": "full" if auto_n == len(criteria) else "partial",
        "coverage_statement": f"Auto-checked {auto_n}/{len(criteria)}; machine cannot prove conformance (FR-5).",
        "criteria": criteria,
        "reviewer_signoff": False,
        "attribution": ATTRIBUTION,
        "checked_at": _stamp(),
    }


def tokens_emit(doc: dict) -> dict:
    """FR-6: DTCG -> CSS variables + TS-модуль + loss-отчёт dropped/changed/same."""
    css, ts, dropped, changed, same = [":root {"], ["export const tokens = {"], [], [], []
    for name, tok in (doc.get("tokens") or {}).items():
        val = tok.get("$value") if isinstance(tok, dict) else tok
        if val is None:
            dropped.append(name)
            continue
        var = "--" + str(name).strip("{}").replace(".", "-")
        css.append(f"  {var}: {val};")
        ts.append(f'  "{name}": "{val}",')
        same.append(name)
    css.append("}")
    ts.append("} as const;")
    return {
        "css": "\n".join(css),
        "ts": "\n".join(ts),
        "loss_report": {"dropped": dropped, "changed": changed, "same": same},
        "attribution": ATTRIBUTION,
        "checked_at": _stamp(),
    }
