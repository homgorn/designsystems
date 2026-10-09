# 01. Обзор сайта designsystems.one

**URL:** https://www.designsystems.one · **Автор:** Kiryl Zhukouski (Design Lead, Познань, remote) · **Слоган:** «Design systems, explained.»

## Одна таблица

| Факт | Значение | Откуда |
|---|---|---|
| Что это | Курируемая галерея реальных design systems + AI-ready аудит + бесплатные tools | `/`, `/about` |
| Систем в каталоге | **120** заявлено; 125 слагов в sitemap; **49** с полными разборами | sitemap, `/api/design-systems` |
| AI-ready индекс | **37** систем × 5 сигналов, аудит 2026-09-04, следующий 2026-12-04, CC BY 4.0 | `/api/ai-ready/systems` |
| Лидер индекса | **Carbon (IBM) — 4/5**; 5/5 нет ни у кого | БД: `ai_ready_systems` |
| Инструментов | **8** бесплатных (токены, a11y, ROI, diff, grid, release, scanner, agent-check) | sitemap `/tools/*` |
| Машинный слой | MCP **23 tools / 3 prompts / 5 resources**, без авторизации; `llms.txt` + `llms-full.txt`; shadcn-реестр `/r` (4 items); JSON-API | `/api/mcp`, `/r`, robots |
| Платное | Agent-Ready Starter **$99** — собран, **«Not on sale yet»**; треки Migrate/Scale/Handoff — заявлены | `/products/*`, `/about` |
| Донат | Buy Me a Coffee — **1 supporter** | BMC-страница |
| Email-захват | **Отсутствует полностью** | аудит страниц |
| Стек | Next.js + Vercel, аналитика Plausible, трекеров и рекламы нет | HTTP-заголовки |
| SEO-позиция | robots разрешает **поимённо 20+ AI-ботов** (GPTBot, ClaudeBot, Perplexity, Google/Apple-Extended, Meta…) | robots.txt |
| Возраст | Первый Wayback-снимок 03.2025; в Tranco top-1M отсутствует; LinkedIn — 26 подписчиков | Wayback, Tranco, LinkedIn meta |
| Трафик | **300–2 000/мес [наша оценка, 4/10]** vs **11 000 [заявление автора, 4/10]** — не сошлось, см. открытые вопросы | `research/01` §3 |

## Позиционирование автора (дословно, `/about`)

- *«Everything here is free and ad-free»* — реклама отвергнута сознательно.
- *«The Build playbook (eight chapters) stays free forever»* — ядро удерживается бесплатным.
- *«Future paid tracks (Migrate, Scale, Handoff) are clearly separated when they ship»* — платная линейка спроектирована.
- Консалтинг: *«from short audits (2-3 weeks) to multi-quarter system builds»* + воркшопы + fractional lead + бесплатный 20-мин звонок.

## URL-инвентарь (223 в sitemap)

design-systems 158 · playbook 15 · foundations 12 · ai-ready 10 · tools 9 · designops 6 · blog 4 (3 поста, 07–09.2026) · products 1.

**Дисциплина данных — сильная сторона:** 120/49/37 согласованы между страницей, API и llms.txt (у конкурентов счётчики расходятся). Единственное расхождение: H1 «100 systems» при тексте «120».

## Уверенность

Факты продукта и инвентаря — **9/10** (прямой фетч). Трафик и выручка — **3–5/10** (внешних источников нет).
