# TODO — главный движок + модули + адаптеры

> Метод: SDD/BMAD, spec-first (без апрува спеки кода нет), скиллы: deep-research-alireza, competitive-teardown-alireza, spec-driven-workflow-alireza.
> Правило для всех: **НИЧЕГО не удалять без двойного подтверждения человека** (см. AGENTS.md).
> Легенда: `[ ]` todo · `[~]` в работе · `[x]` done · `[?]` ждёт решения человека.

## Chunk 0. Фундамент проф. разработки (P0)

- [x] Git: baseline `8e45666` + 3 коммита, дерево чистое (09.10) ✅
- [x] `pyproject.toml`, `.env.example`, `.gitignore` (+*.bak*), pre-commit-конфиг, CI-файл ✅
- [x] `tests/`: **16 passed, 1 skipped, 3 xfailed; покрытие engine 90% (NFR-3 ✅)** (09.10)
- [x] Линт: 16 ошибок ruff → 0; format применён ✅
- [x] `AGENTS.md`, CONTRIBUTING, CHANGELOG (0.1.1), LICENSE, docs/adr ×2, docs/runbook.md ✅ (NFR-4 ✅)
- [x] Конфиг + error-коды ✅ · Фикс «22→23» ✅ (бэкап `.bak-22to23`, `scripts/fix_22to23.py`)
- [x] Найден и исправлен баг тестом: evidence терял причину пробы ✅

## Chunk 1. Анализ рынка скиллом (teardown-lite) — агент R1

- [x] Черновик: 12 измерений × 3 фокуса + карта + action-план → `research/07` §1 (мной, 08.10)
- [~] R1-fill (цены-ревью-вакансии): субагент rate-limited ×2, websearch 401 → §1.1 частичный статус, повтор по готовности квоты (промпт в `tasks/BOARD.md`)
- [?] D1: какой конкурент — главный бенчмарк для P1/P5/P11? (голосование: wiki/13)

## Chunk 2. Дип-рисерч ландшафта движка (выполнен мной 08.10: 6 первичных фетчей)

- [x] H1–H4 + адверсариал + refresh targets → `research/07` §2 ✅ (D2/D3 закрыты кодом: офиц. SDK + argparse)
- [ ] `research/raw/engine/` per-source файлы + повтор R1 при квоте (промпты в `tasks/BOARD.md`)

## Chunk 3. Спека движка (spec-driven, RFC 2119) — агент S1

- [x] `specs/003-engine/spec.md` написана (мной, 08.10)
- [x] S1-валидация: субагент rate-limited → вручную: score 76 → фиксы (AC-11, EC-6, xfail AC-7/8/10) → **84/100 ✅**, pytest 8 passed + 1 skipped + 3 xfailed
- [ ] Твой апрув спеки → разблокирует Chunk 4 (E1)
- [x] Открыто к релизу было: NFR-3 ✅ (90%), NFR-4 ✅ (runbook) — закрыты 09.10, остался твой апрув

## Chunk 4. Ядро движка (реализовано мной 08.10, ждёт ревью — не агента)

- [x] `engine/`: config/corpus/index/checks/exporters/cli/mcp_server ✅ (живой check 3/5, 09.10)
- [ ] Human code review (см. ответ в чате — чеклист) → только потом Chunk 5/6

## Chunk 5. Модули P1/P5/P11 — агенты M1/M2/M3 (параллельно после ядра)

- [ ] `modules/p1_ci/` (Action + раннер + бейдж), `modules/p5_vpat/` (сканер + ACR-сборщик), `modules/p11_kit/` (6 компонентов + 2 skills)
- [ ] Каждый: README lane-границы + тесты из AC спеки

## Chunk 6. Адаптеры — агенты A1/A2 (параллельно после ядра)

- [ ] Tier-1: `adapters/shadcn/`, `adapters/figma/` (variables+Code Connect), `adapters/storybook/`, `adapters/style_dictionary/`
- [ ] Tier-2: `adapters/tokens_studio/`, `adapters/swiftui/`, `adapters/compose/` (генерированные, verify на реальном компоненте)
- [ ] Контракт адаптера: `extract → normalize(DTCG) → emit → verify` (единый интерфейс всех адаптеров)

## Chunk 7. Evals + релиз — агент R3

- [ ] Ночной eval-ран (20 задач × 2 модели, hit-rate), ledger как у Astryx (публикуем и поражения)
- [ ] `CHANGELOG`, версионирование `engine/__init__.py`, релиз-чеклист (см. wiki/09 gaps: MCP-ревизия!)

## Что пропущено для проф. разработки (добираем в Chunk 0/7)

1. Git + ветвление (main/dev/feature/*) и защита main · 2. Тесты: unit+integration+e2e-ежедневный eval · 3. Линт/формат (ruff) + типы (mypy-lite) · 4. Pre-commit + CI + бейджи · 5. Секреты: только env, `.env.example`, сканер секретов · 6. Логи/трейсинг + error-коды · 7. Конфиг окржуениями (dev/ci/prod) · 8. Версии данных: `crawl_meta` + sha + refresh-протокол · 9. Миграции схемы БД (номер версии в `crawl_meta`) · 10. Доки: README/diataxis (how-to/reference), ADRs, runbook · 11. Лицензии: код vs CC BY-данные, атрибуция в каждом экспорте · 12. Security: no-auth поверхности задокументировать + rate-limit план · 13. Perf-бюджеты (NFR: check <30с, FTS <500мс) · 14. Бэкапы `db/` + reproduce `build_db.py --refresh` · 15. Релиз-процесс: spec→tests→impl→review→changelog→tag.

## Порядок запуска агентов

R1+R2 (параллельно) → S1 → E1 → M1/M2/M3 + A1/A2 (параллельно) → R3. Всего 8 агент-задач в `tasks/`.
