# Changelog (Keep-a-Changelog)

## [0.1.1] - 2026-10-09
### Fixed
- Покрытие engine 68% → **90%** (NFR-3 ✅, `tests/test_cli_index.py`)
- Линт: 16 ошибок ruff → 0; сужение `except`, format
- `checks`: evidence хранит причину пробы (`not found (unreachable…)`) — найдено тестом
- БД: note «22 tools» → «23 tools» (`scripts/fix_22to23.py`, бэкап `.bak-22to23`)
- Repo: git-baseline, pre-commit, runbook, ADRs, LICENSE (MIT + CC BY)

## [0.1.0] - 2026-10-09
### Added
- `engine/`: config/corpus/index/checks/exporters/cli/mcp_server (spec 003, score 84/100)
- `tests/`: AC-1–6/9/11, EC-6; xfail AC-7/8/10 (чанки A1/A2)
- `specs/001-003`, `tasks/BOARD.md`, `TODO.md`, `AGENTS.md`
- CI `.github/workflows/ci.yml`, Makefile, pyproject, .env.example
- git-baseline `8e45666` (116 files)
