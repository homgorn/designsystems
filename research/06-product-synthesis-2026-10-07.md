# 06. Синтез новых продуктов 07.10.2026 — из корпуса + рисерчей

> Метод: скиллы `marketing-product-ideas-mia` (5 слоёв + 30 принципов), `product-positioning-mia`, `portfolio-positioning-mia` (architect).
> Валидация: 10 поисков 07.10 (итого 24 за день) — eval-цены, VPAT-тарифы, ROI-тулы, Code Connect, мультибренд, native, agent-UI, paid-skills, DTCG-валидаторы, enterprise API.
> Каждый продукт: актив → разрыв → покупатель → якорь → MVP → ров → риск → уверенность /10.

## Активы (что переиспользуем)

A1. 49 разборов (governance, known-for, watch-outs, anchor-компоненты, token snapshot) · A2. Индекс 37×5 с evidence-URL и ре-аудитом 04.12.2026
A3. 8 tools (генератор с curl, чеклист, ROI-кальк, diff, сканер сайта, Agent-Ready Check POST) · A4. MCP 23 tools no-auth
A5. `/r` 4 items (vs 12 в ките) · A6. Playbook 8+5, foundations 11, glossary 40 · A7. SKILL.md 10 + agent-files 9 (CC0)

## Разрывы (что болит, с доказательством)

G1. ROI измеряют 5%, buy-in 32% (DSR n=147) · G2. code→design умеют 11% · G3. registry=yes 1/37, Code Connect 3/37
G4. eval-харнесс продают 0 игроков (бенчмарки публикуют 3) · G5. agent-UI поставляют 0/21 · G6. DESIGN.md-галереи берут количеством (108–121)
G7. VPAT нужен закупкам (ADA Title II дедлайны 04.2027/04.2028), аудит $1 850–4 450, сканеры ловят ~25–30% · G8. нативный паритет без turnkey-решения

## Продукты: 6 очевидных + 6 неочевидных

### Очевидные (дожать существующее)

| # | Продукт | Актив→разрыв | Покупатель | Якорь | MVP | Уверенность |
|---|---|---|---|---|---|---|
| P1 | **Agent-Ready CI** — eval-харнесс как сервис: N задач × 3–5 моделей, hit-rate, hallucination rate, дашборд, бейдж, GitHub Action | A3(POST-check)+A2 → G4 | DS-лид, platform-инженер | $99–499/мес + usage (HAL-ран $0.10–2 829 подтверждает usage-модель) | недели: POST + раннер + дашборд | 7/10 |
| P2 | **DESIGN.md Export Pack** — 49 разборов → DESIGN.md + реестр-бандл с evidence | A1+A2 → G6 | AI-инженер, vibe-кодер | $49–99 one-time / $19 мес фид | дни: генератор из БД | 7/10 |
| P3 | **Registry Pro** — /r 4→10 + приватные реестры + Code Connect-маппинги | A5 → G3 | DS-инженер | $19–49/мес | недели | 6/10 |
| P4 | **ROI Autopilot** — adoption + drift-скор 0–100 + exec one-pager, непрерывно | A3(ROI-кальк) → G1 | DS-лид, директор продукта | $199–499/мес (Componly €350/6 нед — нижний якорь) | недели: CLI-анализатор + дашборд | 7/10 |
| P5 | **VPAT-from-DS** — conformance из Storybook+токенов → draft ACR в структуре ITI | A3(чеклист+сканер) → G7 | SaaS-вендор на гос/edu-закупках | draft $299 / подписка $249 мес (якорь acrindex); полный аудит $1 490–1 990 (acrdesk) — мы дешевле и непрерывно | недели: сканер + сборщик ACR + coverage statement | 8/10 |
| P6 | **Token Bridge** — audit → token-bridge → componentize → PR в Figma/код | A3(diff)+A6 → G2 | Мигрирующая команда | аудит $4–12k + bridge $2–5k | недели | 6/10 |

### Неочевидные (ставка на пустые клетки)

| # | Продукт | Почему неочевидно | Якорь/прецедент | MVP | Уверенность |
|---|---|---|---|---|---|
| P7 | **Code Connect Packs** — маппинги под ключ на топ-20 систем (.figma.ts + skill + verify через get_code_connect_map) | Все смотрят на MCP, а дыра — в маппингах (3/37); Figma UI+CLI уже сделали механику бесплатной — продаётся работа, не тул | Воркшоп $2–5k; пак $299–999/система | дни на систему | 7/10 |
| P8 | **DTCG Loss-Report CI** — конвертер токенов с отчётом dropped/changed/same + fail-gate (как tokenise, но в CI) | Валидаторы — commodity (tokenise MIT, design-token-kit); продукт — enforcement: «миграция без потерь или красный билд» | $49–199/мес | дни–недели | 6/10 |
| P9 | **Multibrand Graph** — «бренд наследует систему + дельта», per-brand pipeline, темизация 50+ | Кросс-библиотечные алиасы у 21% — боль есть, продукта нет; продаётся не тема, а граф наследования | $499–2k/мес enterprise | недели | 5/10 |
| P10 | **Native Parity CI** — DTCG → SwiftUI + Compose + Flutter + скриншот-diff на устройствах в CI | Все пайплайны кончаются на CSS; turnkey-решения нет (только статьи и Theo JSON/XML) | $399–999/мес | месяц | 5/10 |
| P11 | **Agent-UI Kit** — 16 паттернов (plan, step-ledger, tool-call card, permission gate, result summary, undo) как shadcn-реестр + skills | 0/21 систем поставляют; у всех только «чат-бабл + спиннер» (setproduct); спрос: 46% команд экспериментируют с AI | $99–349 one-time + paid skills ($10–15 прецедент agensi.io; daisyUI Charts/Dashboard) | недели: реестр + 2 skills | 7/10 |
| P12 | **Benchmark Feed** — индекс как версионированный data-продукт: JSON/CSV/SQLite/MCP с SLA и свежестью | Данные CC BY — distribution; продаётся свежесть и SLA, не байты; «registry of registries» для курсов/блогов/тулов | free CC BY + $1–5k/мес спонсор-фид / $15–50k/год enterprise | дни: версионирование + changelog | 7/10 |

## Приоритет (ICE-lite)

P5 (8) > P1=P4=P11=P7=P2=P12 (7) > P3=P6=P8 (6) > P9=P10 (5). Топ-3 в детальную спеку: P1, P5, P11.

## Связка со скиллами

- 5 слоёв: боль — слой 1 (buy-in падает, закупки требуют ACR, агенты галлюцинируют); позиционирование — слой 2 (категория «agent-ready», не «каталог»); ценность — слой 3 (результат: adoption, conformance, hit-rate); трение — слой 4 (POST в CI, one-click DESIGN.md, draft вместо blank page); дистрибуция — слой 5 (CC BY-встраивания, skills-маркетплейсы, реестры).
- Принципы: Proof Over Promise (evidence-URL, coverage statement), Loss Aversion (красный билд, stale-алёрты), Leverage (один корпус → 12 продуктов), Category (мы — «слой выбора и проверки», не галерея).

## Поисковый лог (10)

eval-harness pricing/costs · VPAT/ACR automation cost · ROI/adoption dashboards (Supernova/zeroheight/Componly/Variantly/Buoy/Luro) · Code Connect CLI+UI · multibrand tokens · native SwiftUI/Compose · agent-UI patterns · daisyUI paid skills + skills marketplace · DTCG validator/converter · enterprise API pricing.
