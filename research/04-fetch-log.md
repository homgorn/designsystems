# Fetch-лог: что скачано с designsystems.one 06–07.10.2026

Все запросы — публичные GET без авторизации. User-Agent: браузерный / `designsystems-research/1.0`.

## Артефакты (research/raw/)

| Файл | URL | Размер | Что внутри |
|---|---|---|---|
| `design-systems.html` | `/design-systems` | 529.9 КБ | SSR-HTML галереи (Next.js); 125 слагов `/design-systems/*` |
| `api-design-systems.json` | `/api/design-systems` | 14.2 КБ | `count: 49` — slug, name, company, url, tagline, breakdownUrl |
| `api-ai-ready.json` | `/api/ai-ready/systems` | 79.2 КБ | `count: 37`, `auditedAt: 2026-09-04`, `nextAuditAt: 2026-12-04`, лицензия CC BY 4.0; на систему: score 0–5, 5 сигналов с evidence |
| `api-ai-ready.csv` | `/api/ai-ready/systems.csv` | 11.8 КБ | Табличная версия индекса |
| `api-glossary.json` | `/api/glossary` | 20.6 КБ | 40 терминов с определениями |
| `mcp-discovery.json` | `/api/mcp` | 1.4 КБ | MCP 1.1.0, протокол 2025-06-18, transport streamable-http, **23 tools / 3 prompts / 5 resources**, auth none; self-audit score 4/5 (codeConnect: no) |
| `registry-index.json` | `/r` | 1.1 КБ | shadcn-spec: **4 items** (utils, button, input, card) |
| `llms.txt` | `/llms.txt` | 17.1 КБ | Карта сайта для LLM: API, registry, 10 SKILL.md (CC0), паттерны, playbook 8+5 глав, tools, 49 разборов, foundations |
| `llms-full.txt` | `/llms-full.txt` | 30.7 КБ | Полная версия карты |
| `sitemap.xml` | `/sitemap.xml` | 37.1 КБ | **223 URL**: design-systems 158, playbook 15, foundations 12, ai-ready 10, tools 9, designops 6, blog 4, products 1 |
| `robots.txt` | `/robots.txt` | 2.5 КБ | Allow `/` всем + **поимённо 20+ AI-ботов** (GPTBot, ClaudeBot, PerplexityBot, Google-Extended, Applebot-Extended, Meta-ExternalAgent…); Disallow только `/admin/`, `/dashboard/`; заявлены `/llms.txt`, `/llms-full.txt` |
| `breakdowns/*.json` | `/api/design-systems/{slug}` | 2.7–5.1 КБ × 49 | Полные редакционные разборы всех 49 систем |

## Сводка по БД (db/designsystems.db, SQLite, ~963 КБ)

| Таблица | Строк |
|---|---|
| design_systems / breakdowns | 49 / 49 |
| ai_ready_systems / ai_ready_signals | 37 / 185 |
| breakdown_links (docs/repo/figma/npm/…) | 241 |
| glossary | 40 |
| mcp_tools / prompts / resources | 23 / 3 / 5 |
| site_urls | 223 |
| gallery_only (слаги без разбора) | 76 |
| monetization_surfaces | 17 |
| corpus_fts (entity: design_system, breakdown, ai_signal, glossary) | 323 |

## Распределение AI-сигналов (37 систем × 5)

| Сигнал | yes | no | unknown | n/a |
|---|---|---|---|---|
| mcp | 12 | 20 | 5 | 0 |
| llmsTxt | 10 | 9 | 18 | 0 |
| dtcg | 6 | 15 | 13 | 3 |
| registry | 1 | 36 | 0 | 0 |
| codeConnect | 3 | 21 | 12 | 1 |

Топ по score: Carbon 4/5 → Primer 3/5, shadcn/ui 3/5 → восемь систем 2/5 (Ant, Atlassian, Backpack, Chakra, MUI, Mantine, Spectrum…) → хвост 0–1/5. **5/5 нет ни у кого.**

## Не скачано (следующий проход)

- 49 HTML-страниц разборов (скриншоты, token snapshot в рендере) — взять при необходимости визуального аудита;
- `/tools/*` интерактив (token-generator state, ROI-калькулятор) — только через браузер;
- `/products/agent-ready-starter/walkthrough` — спецификация $99-кита (есть в отчёте 01);
- Plausible-статистика — закрыта (нужен доступ автора).

## Воспроизводимость

`scripts/build_db.py [--refresh] [--skip-breakdowns]` — пересобирает БД из кэша (без сети) или с сети при `--refresh`. `scripts/query.py` — CLI-доступ: `stats|top|signals|system|search|glossary|money|sections|links`.
