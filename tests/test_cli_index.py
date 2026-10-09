"""NFR-3: дотянуть покрытие engine до >=80%. Живые пути CLI/index/corpus."""

from engine import corpus
from engine import index as idx
from engine.cli import main
from engine.config import db_path, figma_token


def test_index_score_carbon():
    s = idx.score("carbon-design")
    assert s["score"] == 4 and s["max"] == 5 and isinstance(s["unknown"], list)


def test_index_top():
    assert idx.top(3)[0][0] == "carbon-design"


def test_corpus_search_and_schema():
    assert corpus.search("token migration", 5) is not None
    assert corpus.schema_version() >= 0
    assert db_path().exists()


def test_corpus_unknown_slug_error():
    import pytest

    with pytest.raises(corpus.CorpusError):
        corpus.signals("no-such-system")


def test_corpus_missing_db_hint(monkeypatch):
    import pytest

    monkeypatch.setenv("DS_DB", "nope/missing.db")
    with pytest.raises(corpus.CorpusError) as e:
        corpus.counts()
    assert "build_db" in str(e.value)


def test_config_figma_token_absent_or_str():
    assert figma_token() is None or isinstance(figma_token(), str)


def test_cli_stats_export_audit(capsys):
    assert main(["stats"]) == 0
    out = capsys.readouterr().out
    assert '"design_systems": 49' in out
    assert main(["export", "carbon-design"]) == 0
    assert "DESIGN.md" in capsys.readouterr().out
    assert main(["export", "nope"]) == 2
    assert main(["audit", "token"]) == 0


def test_checks_unreachable_marks_evidence(monkeypatch):
    import urllib.request

    from engine.checks import check

    def boom(*a, **k):
        raise OSError("net down")

    monkeypatch.setattr(urllib.request, "urlopen", boom)
    res = check("https://example.invalid")
    assert res["score"] == 0
    assert all(c["status"] in ("no", "unknown") for c in res["checks"])
    assert "unreachable" in res["checks"][0]["evidence"]
