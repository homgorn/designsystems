# 02. Продукт послойно

## Галерея (120 систем, 49 разборов)

Ядро — `/design-systems`: карточки реальных систем от Material/Carbon/Polaris до Poncho (Аргентина) и DKFDS (Дания). 49 «якорных» систем имеют редакционный разбор: origin, governance, known-for, watch-outs, evaluation, anchor-компоненты, token snapshot, внешние ссылки (все 241 ссылка — в БД `breakdown_links`: docs/repo/figma/npm/blog).
Полный список 49 — `db.design_systems`; запрос: `python scripts/query.py system <slug>`.
Остальные 76 слагов (`gallery_only`) — карточки/служебные страницы без разбора: широта = long-tail охват.

## Agent-Ready Index (37 × 5)

`/ai-ready/systems`: независимый аудит по сигналам **MCP · llms.txt · DTCG · registry · Code Connect**, только first-party доказательства, квартальный ре-аудит. Данные CC BY 4.0 (JSON + CSV) — валюта цитирования.
Факт из БД: `registry=yes` — **1/37**; `dtcg=yes` — 6; `mcp=yes` — 12; `codeConnect=yes` — 3. Self-audit самого сайта — 4/5 (нет Code Connect), из таблицы не выведен — редкая честность.

## Сквозные срезы

- **12 паттернов** (`/design-systems/patterns/*`): таблицы, формы, confirmations, empty states, навигация, voice, command palette, фильтры, дашборды, dark mode, motion, focus — каждый с 3–4 каноническими системами.
- **20 кросс-ссылок по компонентам** (`/design-systems/components`): один компонент — ответы всех систем (IndexTable vs DataGrid vs DataTable) + editorial note.
- **Compare** (`/design-systems/compare`): 2–3 системы side-by-side, shareable URL.

## Playbook (8 + 5 глав)

Build: should-you-build → foundations → tokens → right-ten-components → patterns → distribution → governance → measuring-value. Migrate: audit → token-bridge → componentize → engineering-path → adopt. Тон — практик, opinionated, ссылки на канонические примеры вместо теории. Это же — контент-база будущего курса ($400–900/место).

## Foundations (11) + Glossary (40) + Frameworks

Цвет, типографика, спейсинг, layout, motion, duration/easing, a11y, voice&tone, нейминг, maturity model. Глоссарий — plain-language, доступен JSON (`/api/glossary`, 40 терминов — все в БД).

## Tools (8, бесплатны)

| Инструмент | Сила |
|---|---|
| Token Generator | OKLCH 11-ступеней через hex-600, APCA+WCAG, 11–12 форматов (CSS, Tailwind 4/3, SCSS, TS/JS, JSON, W3C DTCG 2025.10, Style Dictionary, Tokens Studio), pair finder, brand kits, shareable URL, **curl-экспорт**, one-click в checklist |
| Accessibility Checklist | WCAG 2.1 + in-page contrast tester, принимает киты из генератора |
| ROI Calculator | Скорость/качество/онбординг при внедрении DS |
| Token Diff | Diff двух китов (ребренды, миграции) |
| Grid Builder | Responsive-сетки визуально |
| Release Checker | SemVer + breaking changes + notes |
| Website→Design.md scanner | Сайт → измеренный гайд |
| Agent-Ready Check | Публичный POST для CI |

Конкуренты-генераторы (7 найдено) — все без API-доступа. Это преимущество — в БД `monetization_surfaces`.

## Registry + MCP + API

- `/r` — shadcn-spec (utils, button, input, card), установка `npx shadcn add`. Тонкий free-tier (4 vs 12 в платном ките) — gap для апселла.
- MCP `/api/mcp` — 23 tools (поиск, разборы, сравнение, паттерны, playbook, glossary, генератор токенов, registry, design.md, 10 SKILL.md, индекс, аудит любого docs-сайта), 3 prompts, 5 resources, **no auth**. Сейчас — чистый расход без воронки.
- API: `/api/design-systems[/{slug}]`, `/api/ai-ready/systems[.csv]`, `/api/glossary`, `/api/tokens` (генерация по URL-параметрам) — всё бесплатно и открыто.
- 10 SKILL.md (CC0, без email) + 9 шаблонов agent-файлов — дистрибуция в Cursor/Claude Code/Copilot.
