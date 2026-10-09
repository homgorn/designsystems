# 05. Дип-рефреш 07.10.2026 — живой статус + рынок + конкуренты

> **Метод:** 14 веб-поисков + 3 живых фетча (/, /products, /api/ai-ready) + верификация БД через `scripts/query.py`.
> Субагенты (3× general) — не запустились: rate limit провайдера, задокументировано. Работа выполнена вручную тем же планом.
> Каждый факт — с URL и уверенностью /10. Нет данных = `[нет данных]`.

## 1. Живой статус designsystems.one (07.10.2026)

| Факт | Значение 07.10 | Изменение с 06.10 | Уверенность |
|---|---|---|---|
| Сайт жив | Да, `/` отдаёт «A curated gallery of 120 real-world design systems» | Без изменений | 10/10 |
| `/products` жив | Да; структура «Everything paid here has a free counterpart»: Migrate Playbook ↔ free track, ROI Kit ↔ free calculator, Agent-Ready Starter ↔ free `/r` | Уточнение модели paid↔free (раньше не фиксировали) | 9/10, https://www.designsystems.one/products |
| Каталог | 120 заявлено; галерея `/design-systems` пишет «100 Real-World Examples» в title | Расхождение 100 vs 120 сохраняется | 8/10 |
| AI-ready | 37 систем, re-audit 2026-09-04; API отвечает | Без изменений | 9/10 |
| Трафик: заявление автора | 11 000 визитов/мес, LinkedIn 29.09.2026 | Подтверждено, без нового заявления | 4/10, linkedin.com/posts/kzhukovsky_…-7510660515656798208 |
| Трафик: сторонняя оценка | **2 879 визитов/мес, global rank 4 125 146**, bounce 45%, 3.8 стр/визит, 30 сек | НОВОЕ: поддерживает вилку 300–2 000, а не 11 000 | 5/10, linkedin.com/company/designsystems-one (виджет) |
| Checkout $99 | `[нет данных]` — /products фетч вернул только каркас (JS-рендер цен не виден) | Не верифицировано | 3/10 |
| `/services` | `[нет данных]` — не проверен в этом проходе | Открыт | 3/10 |
| Email-захват | `[нет данных]` — в фетчах `/` и `/products` форм не видно | Открыт | 4/10 |
| BMC supporters | `[нет данных]` — страница не фетчилась в этом проходе | Открыт | 3/10 |

**Вывод по трафику:** три числа на столе — 300–2 000 (наша модель, 4/10), 2 879 (сторонний виджет, 5/10), 11 000 (автор, 4/10). Консенсус смещается к «единицы тысяч», порядок — тысячи, не десятки тысяч. Для revenue-модели использовать 3 000 как базовый сценарий вместо 5 000.

## 2. Рынок: апдейт Q3–Q4 2026

- **Figma Q2 2026 (08.2026, первичный IR):** выручка **$370.1M +48% г/г**, гайд FY2026 поднят до **$1.463–1.467B (+39%)**, NDR **136%**, 80%+ клиентов $10k+ едят AI-кредиты еженедельно, MCP write-to-Figma **+75% кв/кв**, Figma agent — 50%+ крупных клиентов еженедельно. Seats → usage-подтверждено. 9/10. Источники: investor.figma.com, Q2 Prepared Remarks PDF.
- **DTCG 2025.10:** stable без новой версии; 23 adopter'а подтверждены (Adobe, Figma, Framer, Sketch, Penpot, Supernova, zeroheight, Zeplin, Style Dictionary, Tokens Studio…). 8/10. Источники: w3.org/community/design-tokens, designtokens.org/faq.
- **Supernova:** Series A $9.2M (09.2025) подтверждена; цены Pro **$35/место/мес** (yearly) / $45 monthly, 3 000 workspace credits/seat, MCP-лимиты по тирам. 8/10. Источник: supernova.io/pricing, PRNewswire.
- **zeroheight:** Starter **$59/$49** редактор/мес; DSR 2026 подтверждён: n=147, buy-in 32% (было 42%), fully adopted **7%**, ROI измеряют **5%**, недокомплект **61%**. 9/10. Источники: zeroheight.com/pricing, report.zeroheight.com.
- **shadcn → Base UI (07.2026):** дефолт новых проектов — Base UI; Radix поддерживается; заявления «6M+ weekly downloads», «2:1 pick» — из changelog, независимой верификации нет. Тезис «shadcn — дефолт AI-генераторов (v0, Cursor, Copilot, Codex)» подтверждён вторичкой. 8/10. Источник: ui.shadcn.com/docs/changelog/2026-07-base-ui-default.
- **State of AI in DS:** без обновлений с 07.2026 (снапшот 26–28.07, регенерация 21.09). Цифры стабильны: 21 система, 200 affordances, 165 техник, MCP 18/21, skills 18/21. 9/10. Источник: state-of-ai-in-design-systems.netlify.app.

## 3. Конкуренты: рефреш

| Конкурент | Статус 07.10 | Изменение | Уверенность |
|---|---|---|---|
| aidesign.guide | **183 системы, 47 с MCP/Skills/llms.txt, 22 с AI-гайдами**; тиры Free/Pro/Master | Объём и AI-срезы подтверждены вживую | 8/10 |
| Screenrove | **363 скрина**, MCP+REST бесплатны без ключа; сравнительный пост 02.10.2026 | Подтверждено, библиотека выросла | 8/10 |
| registry.directory | **79 реестров, ~27 000 компонентов** (было 86 — пересчёт/чистка); POST /api/submit жив | Число скорректировано 86→79 | 8/10 |
| Into Design Systems | Конф **10–11.03.2027**, Solo **$499**, Team $1 497/$2 495, спикеры Anthropic/OpenAI/Atlassian/Netflix/Yahoo | Даты и цены подтверждены | 8/10 |
| Mobbin | Pro **$10/мес** (yearly) / $15 quarterly; MCP только paid, 60 req/min | Цены подтверждены | 8/10 |
| Refero | Pro ~$10/мес; MCP 8 000 вызовов/мес, нужен paid | Лимиты подтверждены | 7/10 |
| **НОВЫЙ КЛАСТЕР: DESIGN.md-галереи** | **freedesignmd.com (108–121 система, free, без paywall)** · designmd.ai · getmd.design (102 файла) · designmd.directory (87 систем) · freedesign.md (URL→design.md экстрактор) | Не покрыт в research/03 — добавить как B6 | 8/10 |

## 4. Верификация БД (07.10.2026, `scripts/query.py`)

`corpus_fts 323 · design_systems 49 · breakdowns 49 · ai_ready 37/185 · links 241 · glossary 40 · mcp_tools 23 · site_urls 223 · gallery_only 76 · monetization 17` — все счётчики сошлись с wiki. Топ: Carbon 4/5 → Primer 3/5, shadcn 3/5 → восемь систем 2/5. Секции суммируются в 223. Мелочь: note «22 tools» в `monetization_surfaces` при фактических 23 — поправить при следующей пересборке. Уверенность в корпусе — 9/10.

## 5. Что это меняет в выводах

1. Базовый сценарий revenue-модели — **3 000 визитов/мес** (не 5 000): ~$4–7k/мес, консалтинг > продуктов. Потолок одного человека без изменений.
2. Paid↔free-пары на `/products` — сильный фрейм для копирования (вариант B плейбука): каждый платный артефакт имеет бесплатный аналог-воронку.
3. DESIGN.md-галереи — новый фронт конкуренции за «машинный слой»: количества (100+ систем) против нашей глубины (разборы + индекс + evidence). Ответить: DESIGN.md-экспорт наших 49 разборов.
4. Окно «5/5 нет ни у кого» — открыто; State of AI не обновлялся — наш квартальный ре-аудит (след. 04.12.2026) остаётся дифференциатором.

## 6. Поисковый лог (14 запросов)

1. `designsystems.one Kiryl Zhukouski Agent-Ready Starter $99` 2. `designsystems.one traffic visitors October 2026`
3. `W3C Design Tokens DTCG stable 2025.10 adopters 2026` 4. `Figma revenue Q2 2026 MCP usage-based pricing`
5. `Supernova zeroheight funding pricing 2026 design systems` 6. `aidesign.guide design systems catalog AI pricing Pro Master`
7. `Screenrove MCP free REST DESIGN.md library` 8. `registry.directory shadcn registries how many submit POST`
9. `"State of AI in Design Systems" Kaelig update 2026 MCP skills` 10. `shadcn Base UI default v0 Lovable registry growth 2026`
11. `zeroheight Design Systems Report 2026 buy-in ROI adoption` 12. `"Into Design Systems" conference 2027 tickets directory`
13. `freedesignmd design.md library free 100 design systems` 14. `Mobbin Refero MCP pricing Pro $10 limit 2026`
+ фетчи: `/`, `/products`, `/api/ai-ready/systems` (сырой дамп — в tool-output, не в корпус).
