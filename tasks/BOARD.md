# BOARD — 8 агент-задач (чанки). Dispatch-готовые промпты

> Общее для всех: прочитать `AGENTS.md` + свою спеку; **удаление — только с двойного OK человека**;
> отчёт: файлы + тесты + уверенность /10. Зависимости: R1‖R2 → S1 → E1 → (M1‖M2‖M3‖A1‖A2) → R3.

## R1. Teardown-fill (Chunk 1) — скилл competitive-teardown-alireza

Промпт: «Возьми `research/07-engine-landscape-2026-10-08.md` §1 как черновик. Добери для 9 сущностей (zeroheight, Supernova, Componly, acrindex, acrdesk, freedesignmd, getmd, designmd.directory, aidesign.guide): цены с живых pricing-страниц, ≥20 отзывов assessment (где есть), вакансии-сигналы (1 запрос на компанию). Пересчитай 12 измерений, evidence к каждой клетке. Допиши SWOT ×3 фокуса + action-план. Не выдумывай: нет данных → [нет данных].»
Accept: таблица 12×9 с evidence · 3 SWOT · карта · action quick/mid/strategic. Out: новый скоринг методики.

## R2. Deep-research refresh (Chunk 2) — скилл deep-research-alireza

Промпт: «Проверь `refresh_targets.md`-список из research/07: python-sdk releases, shadcn registry changelog, SD v4, Tokens Studio pricing, Figma scopes, Vitest addon, ADA даты, acrindex/acrdesk цены. Формат: per-source файлы `research/raw/engine/NN.md` (мета + verbatim-цитата + счёт Credibility/Recency/Bias), дельта-док `research/08-refresh-YYYY-MM-DD.md`, только изменения.»
Accept: ≥6 source-файлов · дельта · обновлённые H-вердикты. Out: полный ре-ран teardown.

## S1. Валидация спеки 003 (Chunk 3) — скилл spec-driven-workflow-alireza

Промпт: «Провалидируй `specs/003-engine/spec.md`: каждое FR имеет AC; каждый AC — Given/When/Then и тестируем машиной; API покрывает все эндпоинты; модели покрывают все сущности; EC на каждую внешнюю зависимость; Out-of-scope явный; NFR с измеримыми порогами. Выдай score/100 + список фиксов. Затем сгенерируй тест-стабы (красные) в `tests/` из AC-1..AC-10.»
Accept: score ≥ 80 · красные тесты AC-1..10 · список фиксов применён в спеку (версией). Out: реализация.

## E1. Ядро движка (Chunk 4) — после апрува S1 человеком

Промпт: «Реализуй `engine/` по спеке 003: config, corpus, index, checks, exporters, cli, mcp_server. Один AC за раз: тест зелёный → suite без регрессий → коммит. Не строить OS-1..OS-5. `make test` зелёный, `engine stats` == 49/37/185/241/40/23/223.»
Accept: все AC-тесты зелёные · self-review чеклист · CHANGELOG-запись. Out: модули/адаптеры.

## M1/M2/M3. Модули P1/P5/P11 (Chunk 5) — после E1, параллельно

- M1: «P1 CI: GitHub Action (check+drift+бейдж), раннер 20 задач, дашборд-JSON. README lane-границы. Spec: specs/002 P1.»
- M2: «P5 VPAT: сканер + Storybook-Vitest импорт + ACR-сборщик (55 критериев, conformance пустые, coverage statement). Spec: specs/002 P5.»
- M3: «P11 kit: 6 компонентов (step/tool-card/permission/plan/result/undo) + 2 skills. Spec: specs/002 P11.»
Accept каждого: тесты из AC спеки зелёные · README · пример запуска.

## A1/A2. Адаптеры (Chunk 6) — после E1, параллельно

- A1 (Tier-1): «shadcn (registry.json validate + install-план), storybook (Vitest-отчёт → находки), style_dictionary (DTCG→CSS/TS + loss-отчёт). Контракт extract→normalize→emit→verify.»
- A2 (Tier-1+2): «figma (Variables GET + Enterprise-fallback-инструкция + Code Connect CLI-шаблон), tokens_studio (GitHub-sync формат), swiftui+compose (generated, verify на 1 компоненте).»
Accept: каждый адаптер — verify-отчёт · Tier-2 помечены generated.

## R3. Evals + релиз (Chunk 7) — последний

Промпт: «Ночной eval: 20 задач × 2 модели (сэмплинг+кэш), hit-rate ledger (публикуем и поражения, как Astryx). Релиз-чеклист: MCP-ревизия актуальна, атрибуции, CHANGELOG, tag. Runbook: rate-limits, бэкап db/, refresh-протокол.»
Accept: ledger-файл · зелёный CI · релиз-чеклист подписан.
