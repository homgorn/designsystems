# Spec 002 — стартовая тройка продуктов (SDD)

> Источники: `research/06`, `wiki/11`. Статус: draft → решение человеком.

## P1. Agent-Ready CI

**Позиция:** для DS-лидов, которым нужен ответ «соблюдает ли агент систему», это CI-гейт, который даёт hit-rate + hallucination rate + бейдж. В отличие от разовых бенчмарков (Astryx, shadcn evals) — continuous, в вашем репо.
**Работает:** подключить GitHub Action (POST /api/agent-ready-check + N задач × модели) → дашборд → бейдж → алёрт на регресс. **MVP:** раннер + 20 эталонных задач из 49 разборов + дашборд. Недели.
**Цена:** $99–499/мес + usage. **DoD:** 3 пилотных репо с зелёным/красным гейтом.

## P5. VPAT-from-DS

**Позиция:** для SaaS-вендоров на гос/edu-закупках это draft ACR из их DS (Storybook + токены + сканер) с evidence и coverage statement. В отличие от сканеров (~25–30% WCAG) — честная граница авто/ручного; в отличие от аудита $1 490–4 450 — непрерывно и дешевле.
**Работает:** скан 25 страниц → 55 критериев ITI-структуры → failures с правилом и разметкой → вопросы на ручное → ре-ран каждый релиз. Подпись — ревьюер клиента. **MVP:** сборщик ACR + evidence-файл + stale-алёрт. Недели.
**Цена:** $299 draft / $249 мес. **DoD:** 2 draft-отчёта, принятых ревьюерами.

## P11. Agent-UI Kit

**Позиция:** для команд с агентными фичами это shadcn-реестр 16 паттернов (plan, step-ledger, tool-call card, permission gate, result summary, undo) + skills. В отличие от систем с «баблом и спиннером» — готовые примитивы делегирования.
**Работает:** `npx shadcn add` + skill в Claude/Cursor → план и tool-карточки из коробки. **MVP:** 6 компонентов (step status, tool card, permission dialog, plan list, result summary, action trail) + 2 skills (charts/dashboard — прецедент daisyUI). Недели.
**Цена:** $99–349 + paid skills $10–15. **DoD:** демо-агент с permission gate и undo.

## Общее правило

Free-аналог у каждого paid · evidence-URL на каждое заявление · дата свежести · CC BY-фид как distribution.
