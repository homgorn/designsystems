# designsystems.one — исследование «фетч + как заработать»

**Папка:** `C:\susa ai\designsystems` · **Дата:** 06–07.10.2026 · **Статус:** ✅ исследование завершено → решение и проект в отдельном чате.

## Что внутри

```
designsystems/
├── README.md                  ← ты здесь
├── wiki/                      ← LLM-вики (старт: 00-INDEX.md)
│   ├── 00-INDEX.md            ← карта + 3 факта + открытые вопросы
│   ├── 01-overview.md         ← обзор одной таблицей
│   ├── 02-product.md         ← продукт послойно
│   ├── 03-monetization.md    ← как зарабатывает + revenue-модель
│   ├── 04-competitors.md     ← конкуренты сжато
│   ├── 05-market.md          ← рынок сжато
│   ├── 06-how-to-earn.md     ← плейбук A/B/C
│   ├── 07-llm-corpus.md      ← схема БД, FTS, правила цитирования
│   └── 08-sources.md         ← все источники
├── research/                  ← сырые дип-рисерчи
│   ├── 01-business-model-monetization.md
│   ├── 02-market-design-systems-2026.md
│   ├── 03-competitive-landscape-2026.md
│   ├── 04-fetch-log.md
│   ├── 05-deep-refresh-2026-10-07.md  ← живой рефреш 07.10 (14 поисков + 3 фетча)
│   ├── 06-product-synthesis-2026-10-07.md ← синтез 12 продуктов (10 валидаций)
│   └── raw/                   ← 11 артефактов + 49 разборов + HTML галереи
├── specs/
│   ├── 001-decision/spec.md   ← SDD-спека решения A/B/C
│   ├── 002-products/spec.md   ← спека стартовой тройки P1/P5/P11
│   └── 003-engine/spec.md     ← спека движка (FR/NFR/AC/EC/API, S1-на-ревью)
├── engine/                    ← ядро: config/corpus/index/checks/exporters/cli/mcp_server (7/7 тестов ✅)
├── modules/p1_ci|p5_vpat|p11_kit ← стабы M1/M2/M3
├── adapters/                  ← shadcn/figma/storybook/style_dictionary + tokens_studio/swiftui/compose
├── tasks/BOARD.md             ← 8 агент-задач R1/R2/S1/E1/M1-3/A1-2/R3
├── TODO.md + AGENTS.md         ← мастер-план + правила (удаление — только с 2×OK)
├── db/
│   └── designsystems.db       ← SQLite ~963 КБ, 16 таблиц, 323 FTS-записи
└── scripts/
    ├── build_db.py            ← пересборка БД (кэш/сеть)
    └── query.py               ← CLI: stats|top|signals|system|search|glossary|money|sections|links
```

## Короткий ответ на «фетч и как заработать»

**Фетч:** весь машинный слой сайта скачан и нормализован — 49 разборов, 37 AI-аудитов × 5 сигналов, 40 терминов, 223 URL, 23 MCP-tools, 241 внешняя ссылка. Лежит в `db/`, вербатим — в `research/raw/`.

**Как зарабатывает он:** никак ($0). Донат пуст, $99-кит «Not on sale yet», консалтинг без посадочной, email-листа нет. Единственный реальный кэш — консалтинг одного человека.

**Как заработать нам (плейбук — wiki/06):** A) дожать оригинал (Stripe→services→email) · B) скопировать формулу «корпус + считаемый индекс + tools + машинный слой + кит $99 + консалтинг» в смежную нишу из 7 найденных (ROI-измерение, code→design, a11y-VPAT, eval-харнесс…) · C) партнёрство (слой выбора перед Supernova/zeroheight, CC BY-встраивания).

## Уверенность (/10)

Факты продукта 9 · структура рынка/конкурентов 7 · TAM-цифры 4 · трафик (300–2k vs заявленных 11k) 4 · revenue-модель 5.

## Метод

SDD/BMAD: данные (`research/`) → синтез (`wiki/`) → машинный корпус (`db/`) → решение отдельно. Скилл `competitive-intelligence-mia` + 3 фоновых субагента (12–25 поисков каждый, ~60 суммарно).
