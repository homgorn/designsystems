.PHONY: setup lint test query stats
setup:
	python -m pip install -e ".[dev]"
lint:
	python -m ruff check engine tests scripts
test:
	python -m pytest -q
query:
	python scripts/query.py stats
stats:
	python -m engine.cli stats
