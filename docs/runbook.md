# Runbook (NFR-4)

## CI

CI живёт в `.github/workflows/ci.yml` (install → ruff → pytest → query stats).
Локальный эквивалент в чистом venv: `pip install -e ".[dev]" && ruff check … && pytest -q && python scripts/query.py stats`.
⚠️ 2026-10-11: GitHub Actions не стартует — `account is locked due to a billing issue`
(verbatim из check-run annotations, 10/10). Лечится в github.com → Settings → Billing,
затем `gh run rerun <id> --failed`. Код-фикс editable-install при этом верифицирован
в чистом venv локально.

## No-auth поверхности

- MCP (`engine/mcp_server.py`): read-only tools; запись на диск запрещена. План: rate-limit (60 req/min по образцу Mobbin) + allowlist при абьюзе.
- Exports (DESIGN.md/ACR/tokens): публичны, каждый с атрибуцией + checked_at.

## БД
- Бэкап: копия `db/designsystems.db` перед `--refresh`. Reproduce: `python scripts/build_db.py --refresh`.
- Версия схемы: `SCHEMA_VERSION` (`engine/__init__.py` = 1);legacy без `crawl_meta.schema_version` → EC-5.

## Инциденты
- Падающий check: смотреть `evidence` в JSON, затем EC-2/EC-3/EC-4.
- Секреты в логах: ротация + чистка истории (secret-scan в CI — geplant).
