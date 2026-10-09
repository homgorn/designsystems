"""Красная фаза S1: AC-1/AC-2 спеки 003 — счётчики корпуса и скоринг Carbon."""

from engine.corpus import counts, signals


def test_ac1_corpus_counts():
    c = counts()
    assert (
        c["design_systems"],
        c["ai_ready_systems"],
        c["ai_ready_signals"],
        c["breakdown_links"],
        c["glossary"],
        c["mcp_tools"],
        c["site_urls"],
    ) == (49, 37, 185, 241, 40, 23, 223)


def test_ac2_carbon_score_and_evidence():
    sigs = signals("carbon-design")
    yes = [s for s in sigs if s["status"] == "yes"]
    assert len(yes) == 4
    assert all(s.get("source_url") or s.get("evidence") for s in yes)
