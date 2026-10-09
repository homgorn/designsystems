# Конкурентный ландшафт designsystems.one — 2026

> **Происхождение:** competitive-intelligence субагент, 6 октября 2026. **Метод:** 25 веб-поисков + прямая верификация страниц. Скилл: `competitive-intelligence-mia` (пайплайн gather → synthesize → battlecard → validate).
> Трафик — только с источником, иначе `[нет данных]`; Similarweb/Semrush/HypeStat — это `[оценка]`. Уверенность в структуре ландшафта 7/10, в цифрах трафика 4/10.

---

## 0. Эталон: что продаёт designsystems.one

- **Каталог:** 120 систем, **49 с полными разборами** (governance, known-for, watch-outs, anchor-компоненты, token snapshot).
- **Agent-Ready Index:** 37 систем × 5 сигналов. Только first-party доказательства. Аудит 2026-09-04, следующий 2026-12-04. Лидер — Carbon 4/5. JSON+CSV, CC BY 4.0.
- **Инструменты:** генератор токенов (OKLCH/APCA, 12 форматов, DTCG 2025.10), контраст-чекер, ROI-калькулятор, token diff, grid builder, сканер сайтов, **Agent-Ready Check** (публичный POST для CI).
- **Registry** — shadcn-spec, `npx shadcn add`.
- **Платное:** «Migrate Playbook» (PDF), «ROI Kit», «Agent-Ready Starter» (team-shareable лицензия) + Buy Me a Coffee.
- **Трафик:** автор заявлял ~11 000 визитов/мес (LinkedIn, 29.09.2026) `[расхождение оценок — см. 01, вилка 300–2 000]`.

**Стратегический факт:** единственный, кто склеил *каталог* + *независимый AI-аудит* + *инструменты* + *платный продукт*. Конкуренты покрывают максимум два слоя.

---

## A) Прямые конкуренты — каталоги и галереи

| # | Конкурент | URL | Объём | Трафик | Монетизация |
|---|---|---|---|---|---|
| 1 | designsystems.one | designsystems.one | 120 / 49 / 37 | ~11 000 `[заявл.]` | Книги, ROI Kit, Starter, донат |
| 2 | Into Design Systems Directory | designsystems.intodesignsystems.com | 239+ | `[нет данных]` | Конференция от $499 (03.2027), 44 758 подписчиков LinkedIn |
| 3 | UI Systems | userinterface.systems | 187 + 2 676 ссылок | `[нет данных]` | Не указана |
| 4 | designsystems.directory | designsystems.directory | 244 | `[нет данных]` | Нет (донат BMC) |
| 5 | DesignOps World | designops.world | 179 систем / 137 инструментов | `[нет данных]` | Affiliate (раскрыто) |
| 6 | The AI Design Guide | aidesign.guide | 183 системы, 47 с MCP/Skills/llms.txt | `[нет данных]` | Free / Pro / Master |
| 7 | Design Systems Repo | designsystemsrepo.com | ~35 | `[нет данных]` | Не указана |
| 8 | Design System Gallery | designsystem.gallery | н/д | `[нет данных]` | Не указана |
| 9 | designsystem.cc | designsystem.cc | 82 | `[нет данных]` | Не указана |
| 10 | The Component Gallery | component.gallery | 60 / 95 / 2 671 пример | `[нет данных]` | Нет |
| 11 | awesome-design-systems | github.com/alexpate/awesome-design-systems | 200+ | 25 370 ★, 1 627 форков | Нет (Unlicense) |
| 12 | State of AI in Design Systems | state-of-ai-in-design-systems.netlify.app | 21 / 6 платформ / 200 affordances | `[нет данных]` | Нет, CC BY 4.0 |

**Ключевые разборы:**
- **Into Design Systems** — каталог как воронка конференции ($499/билет, спикеры Anthropic/OpenAI/Atlassian/Netflix). Метаданные бедные. Модель «директория как лид-магнит» designsystems.one не использует.
- **DesignOps World** — 10 директорий, affiliate. Счётчики расходятся (136 vs 179) — болезнь директорий; у designsystems.one 120/49/37 согласованы между страницей, API и llms.txt.
- **The AI Design Guide** — ближайший по духу (AI-фильтры), но фильтр, а не рейтинг: нет баллов, методики, вердикта. Монетизация сильнее (платные гайды, tools.md, Tidy-тулы).
- **awesome-design-systems** — 25 370 ★, +600/мес, 160 контрибьюторов: крупнейший дистрибуционный актив. Но статичен, без монетизации и API.
- **State of AI in Design Systems** — **самый опасный конкурент**: 200 affordances и 165 техник с дословными сниппетами и URL на утверждение, JSON-близнецы, SQLite, MCP на 9 read-only инструментов, BibTeX. Защита designsystems.one: живой индекс с квартальным ре-аудитом против датированного снапшота.

---

## B) Косвенные конкуренты

### B1. Инспирационные галереи

| Конкурент | Трафик | Монетизация | Агентный доступ |
|---|---|---|---|
| **Mobbin** | ~1.6M/мес `[оценка]` | $10–16/мес | **MCP на платных** |
| **Refero** | `[нет данных]` | $10–20/место | **MCP + Skill** (8 000 выз./мес) |
| **SaaSFrame** | 93 162 `[оценка]` | $14/мес | Нет |
| **Page Flows** | `[нет данных]` | $99/год | Нет |
| **Land-book** | **2.98M** (08.2026) | Реклама | Нет |
| **Lapa Ninja** | ~313.6K `[оценка]` | Реклама | Нет |
| **Godly** | 125.64K (08.2026) | Реклама | Нет |
| **Minimal Gallery** | 49.1K `[оценка]` | Спонсорские слоты | Нет |
| **Screenrove** | `[нет данных]` | **Бесплатно** | **Бесплатный MCP + REST** |

Реальная угроза — **Screenrove**: та же комбинация «библиотека + агентный слой + бесплатно», только на экранах вместо систем; `get_design` отдаёт измеренный DESIGN.md. **Refero** показывает направление: «design research for humans **and AI**».

### B2. Маркетплейсы китов

Untitled UI ($129–$9 999 разово, 10 000+ компонентов) · UI8 (14 332 ресурса) · Craftwork ($8/мес) · **Envato Elements 16.02M** · **ThemeForest 12.28M**. Другой порядок величины, но другой товар: продают результат (ассеты), не выбор.

### B3. Docs-as-marketing и платформы

shadcn/ui (open code + CLI; с 06.2026 GitHub-реестры без сервера) · **registry.directory** (86 реестров, сабмит одним POST, MCP) · Supernova ($35–45/место, MCP 500→3 000/мес) · zeroheight ($49–59/редактор) · Figma Community (4 770+ китов).
**registry.directory** — образец contributed-каталога, которого нет у designsystems.one: POST-сабмит без аккаунта и PR, аудит записей, MCP.

### B4. AI-генераторы UI (смежный бюджет)

v0 (6M+ devs, $20–100) · Magic Patterns · Lovable ($25–50) · Uizard → Miro. Конкурируют за боль «быстро получить UI», не за выбор системы. designsystems.one на правильной стороне границы («чем строить», не «сгенерируй»).

### B5. Микроконкуренты генераторов токенов

consolelog.tools, oneminutebranding, chromui, pacgie, coloristic, toolzeno, coloursui — все бесплатны в браузере. Преимущество designsystems.one: OKLCH-кривая через hex-600, APCA-матрица 11 ступеней, curl-эндпоинты, DTCG 2025.10, round-trip с Tokens Studio. **API-доступа нет ни у кого из них.**

---

## C) Сводная таблица (сокращённо; полная — в отчёте агента)

| Конкурент | Тип | Объём | Трафик/мес | AI-слой | Главный +/- vs designsystems.one |
|---|---|---|---|---|---|
| Into Design Systems | Каталог+конф. | 239+ | н/д | н/д | +объём/аудитория; −метаданные, аудита нет |
| userinterface.systems | Каталог+комп. | 187+2 676 | н/д | н/д | +кросс-ссылки; −разборов нет |
| designsystems.directory | Список | 244 | н/д | Нет | +скорость; −один мейнтейнер, ноль аналитики |
| DesignOps World | Мультидиректория | 179+137+63 | н/д | н/д | +широта; −affiliate, счётчики врут |
| aidesign.guide | Каталог+гайды | 183/47 AI | н/д | Фильтры+тулы | +артефакты; −нет баллов и методики |
| awesome-list | GitHub | 200+ | 25 370★ | Нет | +дистрибуция; −статичен |
| State of AI in DS | Исследование | 21/200/165 | н/д | MCP+SQLite+BibTeX | +строгость; −снимок, не индекс |
| Mobbin | Экраны | 600k+ | ~1.6M | MCP платный | +аудитория ×100; −другая задача |
| Screenrove | Библиотека+агент | малая/глубокая | н/д | **MCP free** | +DESIGN.md бесплатно; −узкий охват |
| registry.directory | Discovery | 86 реестров | н/д | MCP+POST | +contributed-механизм; −не оценивает системы |
| Supernova/zeroheight | Платформы | — | н/д | MCP | +enterprise; −дорого |

---

## D) SWOT designsystems.one

**S:** единственная связка «каталог+аудит+tools+продукт»; методология (5 сигналов, first-party, ре-аудит, self-score 4/5); данные CC BY как distribution-рычаг; полный агентный стек (llms.txt, markdown, scanner API, registry, design.md); технически сильные tools (OKLCH, APCA, DTCG 2025.10, curl); числовая честность (48/185 unknown задекларированы).
**W:** трафик на 2–3 порядка ниже инфраструктурных; нет contributed-каталога; 48 unknown-ячеек; нет публичного MCP при «MCP must have»-риторике; монетизация без recurring; расхождение «100 vs 120» в H1; нет агентных слоёв у бесплатных продуктов.
**O:** AI-readiness не занят (5/5 нет ни у кого); CC BY-встраивания; слой выбора перед Supernova/zeroheight (партнёрство, не конкуренция); дефицит редакционной глубины; контент «какую выбрать / как мигрировать / сколько стоит».
**T:** демотивация аудита («все провалились»); вертикальный дрейф галерей в MCP; поглощение снизу shadcn-реестрами; свежесть силами одного человека; органика одного автора.

---

## E) Белые пятна

**Нет у designsystems.one, есть у конкурентов:** публичный MCP (8 игроков); contributed-сабмит (registry.directory — один POST); экспорт артефактов (Untitled/UI8); кросс-компонентная база (component.gallery 2 671); живая лента+дайджест; аудитория и соцдоказательство; галереи продуктов как вход.
**Нет у конкурентов, есть у designsystems.one:** независимость аудита с self-scoring; аудит+каталог в одном месте; балльная система с evidence-URL; CI-сканер `/api/agent-ready-check`; curl-экспорт токенов; фильтр «на чём строить»; ценовой якорь «0».

---

## Приоритеты (по отчёту)

1. **Публичный read-only MCP + SQLite поверх JSON** — дни работы, закрывает главный пробел.
2. **Сабмит систем третьими лицами** (API + форма по образцу registry.directory) — сообщество, свежесть, SEO-сигнал.
3. **Догнать State of AI по строгости** — закрыть/переклассифицировать 48 unknown, дословные сниппеты с URL.

**Не делать:** экранные галереи (чужой рынок ×100 денег); affiliate (убивает независимость — единственный актив); гонка трафика с Land-book/Envato (конкуренция за качество ответа, не объём).
