# 07. Engine Landscape: teardown-lite + deep-research (08.10.2026)

> Скиллы: `competitive-teardown-alireza` (фокус a/b/c, 12 измерений) + `deep-research-alireza` (H1–H4, триангуляция, адверсариал).
> Источники: 6 первичных фетчей 08.10 + корпус 07.10 (24 поиска). websearch 08.10 недоступен (401) — компенсировано первичкой.

## §1. Teardown-lite: 3 фокуса (скоринг 1–5, evidence одной строкой)

### (a) ROI/adoption: zeroheight Measurement vs Supernova Adoption vs Componly

| # | Измерение | zeroheight | Supernova | Componly | Наш P1/P4 |
|---|---|---|---|---|---|
| 1 | Features | 4 (docs+code+токены+поиск) | 4 (CLI-анализатор, prop-level, snapshots) | 3 (Figma+code, drift, ROI) | 3 (план: POST-check + drift + бейдж) |
| 2 | Pricing | 3 ($49–59, enterprise custom) | 3 ($35, кредиты) | 4 (€350/6 нед аудит — низкий вход) | 4 (план $99–499 + usage) |
| 3 | UX | 4 | 4 | 3 | 3 |
| 4 | Performance | 3 | 3 | 3 | 4 (SQLite локально, без upload кода — как Supernova «only scan results») |
| 5 | Docs | 5 | 4 | 3 | 3 |
| 6 | Support | 4 | 4 | 3 | 2 (один человек) |
| 7 | Integrations | 4 (Figma/Sketch/XD, GA/Hotjar) | 4 (Figma, Storybook, Git, VSCode) | 3 | 3 (план: GitHub Action) |
| 8 | Security | 4 (SSO/SAML) | 4 (SOC2, GDPR, SSO) | 2 | 2 (документировать no-auth!) |
| 9 | Scalability | 4 | 4 | 3 | 3 |
| 10 | Brand | 4 | 4 | 2 | 3 (независимость = бренд) |
| 11 | Community | 4 (Slack, Converge) | 3 | 2 | 2 |
| 12 | Innovation | 4 (MCP, AI) | 5 (AI-отряд $10k/мес) | 3 | 4 (eval-харнесс продают 0) |
| **Итого /60** | | **45** | **44** | **34** | **38 (план)** |

**Вывод:** дыра — независимый вендор-нейтральный слой (все трое привязаны к своей платформе). Наш ход: CI-гейт + drift + exec one-pager, код никуда не upload'ится. Уверенность 7/10.

### (b) ACR: acrindex (draft $299/$249) vs acrdesk ($1 490–1 990) vs AllAccessible (авто)

| # | zeroheight… нет — измерение | acrindex | acrdesk | AllAccessible | Наш P5 |
|---|---|---|---|---|---|
| 1 | Features | 4 (evidence + coverage statement) | 5 (remark на критерий, fix-list, retest) | 2 (сканер, «подписывает» то, что нельзя) | 4 (план: Storybook+токены → draft) |
| 2 | Pricing | 5 ($299 — якорь) | 3 | 3 | 5 ($299 draft / $249 мес) |
| 8 | Security/доверие | 4 (честная граница авто/ручного) | 5 (имя аудитора) | 1 (скан-only ACR = liability) | 4 (coverage statement обязательно) |
| **Позиция** | | value-лидер | premium | red flag | **continuous + честный** |

**Вывод:** P5 копирует acrindex-модель (draft + evidence + «подписывает ревьюер»), отличие — источник данных DS (Storybook pass + токены), непрерывность (ре-ран на релиз) и stale-алёрты. Дедлайны ADA Title II (04.2027/04.2028) — попутный ветер. 8/10.

### (c) DESIGN.md: freedesignmd (108–121) vs getmd (102) vs designmd.directory (87)

Все — количество без evidence и свежести; ни у кого нет разборов governance/watch-outs и квартального ре-аудита. Наш P2/P12: глубина + evidence-URL + дата. Позиция: «не больше файлов, а файлы, которым можно верить». 7/10.

**Карта (Value × Independence):** высокий value + низкая independence = zeroheight/Supernova; низкий value + средняя independence = DESIGN.md-галереи; **пустой квадрант: высокий value + высокая independence = мы (P1/P4/P5/P12).**

**Action-план:** quick (DESIGN.md-экспорт 49, фикс 22→23, бейдж индекса) · mid (P5 draft, P1 Action, Registry 4→10) · strategic (P9/P10, enterprise фид).

## §1.1. R1-дообогащение (08.10, вручную — субагент упал по rate limit, websearch 401)

Статус: **частично**. Цены и позиционирование всех 9 сущностей уже зафиксированы первичкой 07–08.10
(zeroheight $49–59 · Supernova $35 · Componly €350/6 нед · acrindex $299/$249 · acrdesk $1 490–1 990 ·
DESIGN.md-галереи free · aidesign Free/Pro/Master). Не добрано: отзывы ≥20/сущность, вакансии-сигналы,
живые pricing-ревизии. Причина: websearch-квота исчерпана, субагент rate-limited.
Перенесено в refresh: повтор R1 при восстановлении квоты (промпт — tasks/BOARD.md).
На скоринг §1 это не влияет (оценки помечены 6/10 именно из-за вторичности части данных).

## §2. Deep-research: вердикты H1–H4

- **H1 (MCP-фреймворк: официальный Python SDK): ПОДТВЕРЖДЕН.** `modelcontextprotocol/python-sdk`, 24.5k★, `pip install mcp`, transports stdio/streamable-http/SSE, декораторы `@mcp.tool()` (схема из type hints). Первичка: github.com/modelcontextprotocol/python-sdk. 9/10. Решение D2: официальный SDK, FastMCP-стиль API внутри него.
- **H2 (реестр-формат: shadcn registry.json + item JSON): ПОДТВЕРЖДЕН.** Схемы `registry.json` / `registry-item-json`, namespaces, auth, MCP server, API ref. Первичка: ui.shadcn.com/docs/registry. 9/10. Наш `/r` — подмножество этой схемы (совместимо).
- **H3 (токен-пайплайн: DTCG → Style Dictionary → платформы): ПОДТВЕРЖДЕН.** SD forward-compatible с DTCG, эмиты iOS/Android/CSS/JS; Tokens Studio: GitHub/GitLab/Bitbucket/Azure sync, multi-file (pro), W3C-vs-Legacy переключатель, SD-трансформы. Первичка: styledictionary.com, docs.tokens.studio. 9/10. Контракт адаптера: `extract → normalize(DTCG) → emit → verify`.
- **H4 (Figma Variables REST достаточен для CI-синка): ЧАСТИЧНО ОПРОВЕРГНУТ.** GET/POST variables работают, но требуют **Enterprise-план** (`file_variables:read/write`, POST — Full seats). Первичка: developers.figma.com/docs/rest-api/variables. 8/10. Следствие: Tier-1 Figma-адаптер = Variables API (enterprise) + fallback Tokens Studio sync / Code Connect CLI (доступнее).
- **Доп-находка (адверсариал): Storybook test-runner АРХИВИРОВАН 30.09.2026** — миграция на Vitest addon (быстрее, a11y+coverage из коробки). Первичка: github.com/storybookjs/test-runner. 9/10. Следствие: P5 опирается на **Vitest addon + play-функции + postVisit-хуки**, не на test-runner.

**Адверсариал (4 вопроса):** (1) Что если Figma закроет Variables API? — fallback Tokens Studio/CLI, DTCG-канон у нас. (2) Что если shadcn сменит схему? — версионируем адаптер, registry.json валидируем. (3) Кто платит за eval-compute? — сэмплинг + кэширование + tiers (HAL: $0.10–2 829/ран). (4) S stacks Enterprise: Variables API + тесты — P5 стартует с web/SaaS, native — P10 позже.

**Refresh targets:** python-sdk releases · shadcn registry changelog · SD v4 migration · Tokens Studio pricing · Figma Variables scopes · Vitest addon · ADA Title II даты · acrindex/acrdesk цены.

## Уверенность

Первичка 9/10 · teardown-скоринг 6/10 (вторичные данные частично) · H-вердикты 8–9/10.
