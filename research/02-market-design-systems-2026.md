# Рынок design systems, design tokens и UI-инструментария — 2026

> **Происхождение:** дип-рисерч субагент (general), 6 октября 2026. **Метод:** 22 веб-поиска, приоритет первичным источникам (W3C DTCG, отчётные страницы продуктов, *State of AI in Design Systems* со-председателя DTCG, финансовые отчёты).
> Каждый факт — с URL. Неподтверждённое помечено `[оценка]`. Уверенность в структурных выводах 7–8/10, в цифрах TAM — 4/10 (см. §0).

---

## 0. Предупреждение о цифрах рынка

Категория «design systems software» в отраслевых отчётах — синтетическая. Один запрос даёт цифры с разбросом **190×**:

| Источник | Сегмент | 2025/2026 | Прогноз | CAGR |
|---|---|---|---|---|
| Business Research Insights | «Design systems software» | $0.39 млрд (2026) | $0.87 млрд к 2035 | 9.5% |
| Dataintelo | «Design systems software» | $8.4 млрд (2025) | $22.6 млрд к 2034 | 11.6% |
| Verified Market Research | «Design systems software» | $75.2 млрд (2023) | $115 млрд к 2031 | 4.8% |
| Research and Markets | GUI design software | $30.64 → $34.64 млрд (2026) | $52.54 млрд к 2030 | ~11–13% |
| Cognitive Market Research | Design services | $141.5 млрд (2021) | $186.5 млрд (2026) | 5.66% |

Разброс объясняется границей подсчёта: от лицензий на DS-софт до всех дизайн-услуг. **Цитировать любую цифру как TAM нельзя.** Ниже — bottom-up реконструкция.

---

## 1. Размер и динамика: bottom-up

### 1.1 Слой 1 — «дизайн-платформа» (Figma и аналоги)

Figma — единственный публично отчётный эталон:

| Показатель | Значение |
|---|---|
| Выручка FY2025 | **$1.056 млрд** (+41% г/г) |
| Выручка Q1 2026 | **$333.4 млн (+46%)** |
| Гайд FY2026 | **$1.422–1.428 млрд** (+35%) |
| Net Dollar Retention | 136% |
| Доля среди DS-команд | **97%** используют Figma (DSR 2026) |
| MCP-лимиты | Pro/Org — 200 выз./день; Enterprise — 600/день; Starter — **6 read-вызовов/мес** |

Цены 2026 (seat/мес, годовая): Professional $16 Full / $12 Dev / $3 Collab · Organization $55/$25/$5 · Enterprise $90/$35/$5. Code Connect требует Org/Enterprise. Write-to-canvas в MCP пока бесплатен в бете, заявлен переход на **usage-based**.

### 1.2 Слой 2 — «инфраструктура DS» (настоящий SAM ниши)

| Компания | Выручка / ARR | Источник |
|---|---|---|
| Zeplin | **$51.9 млн** (2024, рост с $32.5 млн) | getlatka |
| Frontify | **$60.3 млн** (2024, рост с $45 млн) | getlatka |
| Chromatic | **$5.6 млн** на 51 чел. (2025) | getlatka |
| Uizard | ~$3.5 млн ARR `[оценка]`; **куплен Miro 06.2024** | tooljunction |
| Supernova | выручка утроена за год, сумма не раскрыта (2025) | prnewswire |
| zeroheight | не раскрывается | — |

**[оценка] SAM слоя 2 ≈ $250–450 млн ARR** (уверенность 5/10): ~83% организаций имеют DS-команду; медиана 3–5 чел.; ACV $15–40 тыс./год; 61% команд недокомплектованы и платят минимально.

### 1.3 Слой 3 — услуги

Design services — $186.5 млрд к 2026: смежный рынок, не tooling.

### 1.4 Динамика

**Драйвер №1 — стандартизация.** 28.10.2025 DTCG выпустила **Design Tokens 2025.10** (первая стабильная): темы и мультибренд, Display P3 / Oklch / CSS Color 4, наследование и алиасы, один файл → iOS/Android/web/Flutter. Статус — Final Community Group Report (не W3C Standard), помечена «stable». 23 adopter'а: Adobe, Figma, Framer, Sketch, Penpot, Supernova, zeroheight, Zeplin, Style Dictionary, Tokens Studio и др.

**Драйвер №2 — adoption токенов:** 84% DS-команд используют токены (2025) против 56% (2024).

**Драйвер №3 — AI:** Supernova Series A **$9.2 млн** (09.2025); Figma подняла гайд на $55 млн из-за AI-адопшена.

**Тормоз №1 — ресурсный кризис** (Design Systems Report 2026, zeroheight, n=147):

| Метрика | 2026 | 2025 |
|---|---|---|
| Выделенная DS-команда | **83%** | 78% |
| Полностью внедрена везде | **7%** | — |
| Довольны поддержкой руководства | **32%** | 42% |
| Недовольны | **40%** | 23% |
| Недокомплектованы | **61%** | — |

Gartner ставит design systems на «Дно разочарования» Hype Cycle 2025.

---

## 2. Ключевые игроки

### 2.1 Дизайн-системы как продукт

| Игрок | Цены 2026 | Funding / ARR |
|---|---|---|
| **Figma** | $16–$90/сеат/мес | $1.056 млрд (2025) → гайд $1.42+ млрд |
| **Supernova** | Free · Pro **$35**/сеат/мес · Enterprise; supernova.ai: AI Data Team от **$10 000/мес** | Series A **$9.2 млн** (09.2025), всего $22.2 млн |
| **Tokens Studio** | Starter Plus **€17**/мес · Essential **€169** · Organization **€499** | 368k пользователей плагина |
| **Style Dictionary** | Бесплатно (MIT) | 4.8k ⭐, **1.73 млн** npm-загрузок/нед. |
| **zeroheight** | Не публикуется | Series A **$10 млн** (2021); всего ~$21.4 млн |
| **Untitled UI** | Figma PRO от **$129** разово · React PRO от **$349** · Studio $399 | 351k пользователей в Figma |
| **Radix** | Free; `shadcn/designer` Business License **$1 499/год** | Принадлежит **WorkOS**; primitives 19.3k ⭐ |

### 2.2 OSS UI-киты

| Библиотека | Масштаб | MCP/agent-готовность |
|---|---|---|
| **shadcn/ui** | **165k** ⭐; **57 млн/мес** npm; 45 млн компонентов/мес через registry | ai-native: 2 MCP, llms.txt, skills, registry, evals.json |
| **MUI** | ~98k ⭐; ~7.3 млн/нед | MCP с платной generateReactCode |
| **Mantine** | 31k ⭐; 1.8–1.9 млн/нед | **3 MCP**, генерирует 4.2 МБ llms-full.txt |
| **Radix UI** | 19.3k ⭐; 4M+/мес | базовый |
| **Chakra UI** | 38.7k ⭐; 533k/нед | MCP разблокирует Pro-шаблоны по API-ключу |
| **Ant Design** | — | `antd mcp`, 2 MCP |
| **daisyUI** | — | **продаёт платные Dashboard и Charts skills** |
| Carbon / PatternFly / Primer | enterprise | ai-native; USWDS — единственный «emerging» |

Сдвиг 2026: **shadcn/ui по умолчанию перешёл на Base UI** (07.2026), дефолт для v0.dev, Lovable, Bolt, Cursor, Claude Code.

### 2.3 Реестры и разработка

Storybook — >50% Fortune 50. Chromatic: $5.6 млн (2025), M&A-оффер 04.2025. Backstage SaaS — Spotify Portal. Code Connect: 248 публичных репо, но реально поставляют **только CDS (~124 файла), Carbon (~86), Primer (52)**.

### 2.4 Стандарты

DTCG 2025.10 stable. Соседи: CSS Color 4, RFC 9727 `api-catalog`, `/.well-known/skills/` manifest (2026, Nord, React Spectrum), `llms.txt`.

---

## 3. Тренды 2025–2026

### 3.1 Дизайн-система стала API для агентов

Первоисточник: [State of AI in Design Systems, 26–28.07.2026](https://state-of-ai-in-design-systems.netlify.app/) (Kaelig Deloumeau-Prigent, со-председатель DTCG, CC BY 4.0). 21 система, 200 AI-возможностей:

| Возможность | Систем из 21 |
|---|---|
| Официальный MCP-сервер | **20** |
| Agent skill (SKILL.md) | **19** |
| `llms.txt` | 15 |
| AGENTS.md/CLAUDE.md в репо | 16 |
| Storybook-интеграция | 14 |
| Реестр компонентов | 11 |
| CLI-скаффолдинг | 9 |
| **Figma Code Connect** | **3** |

Зрелость: **15 «ai-native»**, 5 «invested», 1 «emerging». Три вывода автора: (1) машинный интерфейс — table stakes; (2) контекстные файлы должны быть **компилируемыми, не написанными** (Mantine генерирует llms.txt + mcp/index.json из MDX на каждом релизе); (3) третье поколение — **структурное принуждение**: Polaris «you cannot trust your trained knowledge», Primer «CRITICAL: CALL THIS FIRST», shadcn запрещает тянуть файлы с GitHub вручную.

### 3.2 Опубликованные evals

Atlassian DESIGN.md (80 КБ, head-to-head MCP vs skill vs DESIGN.md vs nothing). shadcn — `evals.json`. **Astryx** — ночной бенчмарк, baseline выиграл **50 из 91 ночи**, все прогоны публикуются включая поражения.

### 3.3 Открытость vs огороженный сад

Nuxt UI: RFC 9727 api-catalog + markdown content negotiation (максимум discoverability). Shopify Polaris: блокирует GPTBot/ClaudeBot, `noai` на страницах, AI-потребление через закрытый toolkit. Обе стратегии сознательные.

### 3.4 Token-driven development

DSR 2026: автоматизации нет у **60%**; design→code у 29%; code→design — **11%**. Главный пробел респондентов: *«Design-to-code parity and handoff»*, *«Token management and syncing»*. Структура токенов: primitive 90%, semantic 85%, **component 52%**. В коде токены у 82%, в документации — **66%**.

### 3.5 «As code» vs «as doc» — вопрос снят

Документация проиграла коду; выиграл **принудительный пайплайн**: MCP + CLI + валидатор — новый дефолт.

### 3.6 AI в процессах

Встроили AI только **10%** DS-команд (как в 2025), **46% экспериментируют**. 61% обеспокоены качеством AI-вывода. AI для документации DS используют **10%** — самая незанятая ниша с высоким потолком.

---

## 4. Что реально зарабатывает (выводы о деньгах)

1. **Деньги — в enterprise-слое.** Zeplin при $1.2 млн инвестиций делает больше Chromatic при M&A-оффере.
2. **Продаётся «результат»:** Frontify — DAM за MAU; Supernova — «AI-отряд» за $10k/мес; Figma — seats + Code Connect за Org/Enterprise.
3. **OSS — витрина, не бизнес.** Монетизация через enterprise-расширения: MUI X, MUI MCP generateReactCode, Chakra Pro по ключу, daisyUI skills.
4. **Инфраструктура схлопывается:** Uizard → Miro; сдвиг в «production-native» (Dessn $6 млн, Paper $34 млн Series A 07.2026).
5. **Якорь сдвигается с seats на usage:** кредиты Supernova, AI credits Figma, Agent Credits Builder.io. «Token Tax»: до **130 кредитов** на сложную сборку в Supernova `[вторичный источник]`.

---

## 5. Барьеры и moat для DesignSystems.One

**Барьеры монетизации:** нет бюджетного мандата (buy-in 32%, падает); покупатель мал (3–5 чел.) и беден; платформа съела discovery (18/21 DS публикуют llms.txt+MCP сами); SEO деградирует от AI-ответов; бесплатный конкурент (designsystems.directory, 244 сайта).

**Четыре реальных moat:** (1) продольный датасет 14 лет — реестра *версий систем* нет ни у кого; (2) нормализованный машинно-читаемый корпус 120+ систем — «контекст для агентов»; (3) слой бенчмарков/evals — evals публикуют только Atlassian, shadcn, Astryx; (4) AEO-монетизация: продавать машине доступ, не человеку чтение («registry of registries»).

**Честно отсутствует:** данные о реальном adoption, права на републикацию, **связь с выручкой** (adoption измеряет 41%, ROI — **5%**).

---

## 6. Семь незанятых ниш 2026

| # | Ниша | Сигнал (первоисточник) |
|---|---|---|
| 1 | **Измерение ROI дизайн-системы** — CI считает adoption + drift-скор 0–100 + one-pager для руководства | ROI измеряют **5%**; buy-in 32%; Mesh Analytics/Observatory строят сами |
| 2 | **Обратный синхрон code → design** — арбитр «дизайн говорит X, код говорит Y» с PR в Figma | code→design умеют **11%**; вендоры не отдают design-as-source |
| 3 | **Нативный паритет** — DTCG → SwiftUI + Compose + Flutter + визуальный diff на устройствах в CI | iOS 35%, Android 34%; пайплайны кончаются на CSS |
| 4 | **A11y как артефакт системы** — conformance по Storybook + VPAT/ACR из DS, бюджет комплаенса | guidelines у 59%, удовлетворённость 44%; сканеры ловят ~25–30% WCAG |
| 5 | **Мультибренд 50+** — токен-граф «бренд наследует систему + дельта», per-brand pipeline | кросс-библиотечные алиасы у **21%**; темизация у 63% |
| 6 | **Eval-харнесс «соблюдает ли агент систему»** — N задач × 3–5 моделей, hit-rate, hallucination rate, дашборд | бенчмарки публикуют 3 игрока; никто не продаёт проверку как сервис |
| 7 | **Компоненты agentного UI** — tool-call timeline, streaming-прерывание, citations, diff-view, permission gate | 0/21 систем поставляют; 46% команд экспериментируют с AI |

Бонус: бренд-токены для печати/моушна/3D (Tokens Studio экспортирует в PPT/Blender, рабочих продуктов нет).

---

## Приложение: три цифры для решения

1. **TAM-разброс 190×** — любая презентация начинается с вопроса о границе подсчёта.
2. **7% полного внедрения** при 83% наличии команд: продавать результат (adoption, ROI, a11y), не артефакты.
3. **20/21 DS уже имеют MCP.** Окно «контекст для агентов» закрывается за 12–18 мес. Окно «контекст *о* системах» (сравнение, бенчмарки, версии) — открыто.

**Счётчик поисков:** 22 · **Первичных источников:** 31
