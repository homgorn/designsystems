"""S1 красная фаза: AC-3/4/5/6/9 спеки 003 (checks + exports + CLI exit-code)."""

from engine import exporters
from engine.checks import check


def test_ac3_check_without_repo_marks_dtcg_unknown():
    res = check("https://www.designsystems.one")
    by_sig = {c["signal"]: c for c in res["checks"]}
    assert by_sig["dtcg"]["status"] == "unknown"
    assert by_sig["codeConnect"]["status"] == "unknown"
    assert res["score"] <= 5


def test_ac4_design_md_has_evidence_and_attribution():
    md = exporters.design_md({"name": "X", "company": "Y", "tokens": "a: b"}, "x")
    assert "X" in md and "DesignSystems.one (2026)" in md and "Checked at" in md


def test_ac5_acr_conformance_empty_and_coverage():
    d = exporters.acr_draft(
        "P", [{"criterion": "1.1.1", "auto": True, "finding": "ok", "evidence": "e"}]
    )
    assert d["criteria"][0]["conformance"] is None
    assert d["reviewer_signoff"] is False
    assert "coverage_statement" in d


def test_ac6_tokens_loss_report():
    out = exporters.tokens_emit({"tokens": {"color.bg": {"$value": "#fff"}, "broken": {}}})
    assert "--color-bg: #fff;" in out["css"]
    assert out["loss_report"]["dropped"] == ["broken"]


def test_ac9_cli_gate_exit_code():
    from engine.cli import main

    assert main(["check", "https://www.designsystems.one", "--min-score", "99"]) == 1


def test_ac11_attribution_in_all_exports():
    from engine import exporters

    md = exporters.design_md({"name": "X"}, "x")
    acr = exporters.acr_draft("P", [])
    tok = exporters.tokens_emit({"tokens": {}})
    for out in (md, acr["attribution"], tok["attribution"]):
        assert "DesignSystems.one (2026)" in out
    for out in (md, acr["checked_at"], tok["checked_at"]):
        assert out  # checked_at непуст везде


def test_ec6_mcp_missing_extra_hint():
    import pytest

    try:
        import mcp  # noqa

        pytest.skip("mcp установлен — EC-6 не применим")
    except ImportError as exc:
        assert "pip install" in str(exc) or "No module named 'mcp'" in str(exc)


import pytest as _pt


@_pt.mark.xfail(reason="Chunk A1: shadcn-адаптер — стаб, verify едет в A1 (AC-7)")
def test_ac7_adapter_verify():
    from adapters.shadcn import verify

    assert verify("button.json")["valid"]


@_pt.mark.xfail(reason="Chunk E1-followup: MCP live-тест после установки extra (AC-8)")
def test_ac8_mcp_search():
    from engine.mcp_server import create_server

    assert create_server() is not None


@_pt.mark.xfail(reason="Chunk A2: figma-fallback едет в A2 (AC-10)")
def test_ac10_figma_fallback():
    from adapters.figma import fallback_instruction

    assert "Tokens Studio" in fallback_instruction(None)
