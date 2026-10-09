# Spec 003 — главный движок Agent-Ready (spec-driven, RFC 2119)

> Статус: Draft · Автор: AI-сессия 08.10.2026 · Ревьюер: человек (апрув нужен до Chunk 4).
> Источники: `research/07`, `specs/002`, `db/designsystems.db`. Формат: spec-driven-workflow-alireza.

## 1. Context

Корпус (49/37×5/241/40/23/223) лежит в SQLite и доступен через `scripts/query.py`, но: нет тестов, нет API-версионирования, нет CI-гейтов, экспорты (DESIGN.md/ACR) отсутствуют, адаптеры не типизированы. Движок превращает корпус в исполняемый слой: `corpus → index → checks → exports`, поверх — модули P1/P5/P11 и адаптеры. Почему сейчас: teardown показал пустой квадрант (value × independence), H1–H4 закрыли выборы фреймворков.

## 2. Functional Requirements

- **FR-1.** Движок MUST читать `db/designsystems.db` (путь из env `DS_DB`, default `db/designsystems.db`) и отдавать: системы, разборы, сигналы, ссылки, глоссарий, MCP-инвентарь, URL-инвентарь.
- **FR-2.** Скоринг MUST повторять методику индекса: 5 сигналов (mcp/llmsTxt/dtcg/registry/codeConnect), score 0–5, evidence-URL обязателен; unknown —显式, не `no`.
- **FR-3.** Раннер проверок MUST принимать `{url, repo?}` и возвращать `{score, checks[5], evidence[], duration_ms, checked_at}`; чек llmsTxt/registry — HTTP GET; mcp — HEAD/GET endpoint; dtcg/codeConnect — только при `repo` (иначе `unknown`).
- **FR-4.** Экспортёр DESIGN.md MUST генерировать файл из разбора: токены, типографика, спейсинг, компоненты, паттерны + evidence-ссылки + `checked_at`.
- **FR-5.** Экспортёр ACR-draft MUST собирать ITI-структуру (55 критериев L-A/AA): автонаходимое (сканер+Storybook-Vitest) → failures с правилом и разметкой; машинно-непроверяемое → вопрос ревьюеру; conformance-уровни MUST оставаться пустыми (решает ревьюер); coverage statement обязателен.
- **FR-6.** Экспортёр токенов MUST принимать DTCG JSON и emit CSS variables + TS-модуль (минимум); loss-отчёт `dropped/changed/same` обязателен.
- **FR-7.** Адаптеры MUST реализовывать `extract → normalize(DTCG) → emit → verify`; Tier-1: shadcn, figma, storybook, style_dictionary; Tier-2: tokens_studio, swiftui, compose (с пометкой generated + verify на реальном компоненте).
- **FR-8.** MCP-сервер (официальный Python SDK, streamable-http) MUST экспонировать read-only tools: `search, get_system, list_signals, run_check, export_design_md` (запись — только run_check по запросу, без persistence).
- **FR-9.** CLI MUST иметь команды `stats|check|export|audit` с JSON-выводом (`--json`) и exit-code ≠ 0 при провале гейта.
- **FR-10.** Каждый экспорт MUST содержать атрибуцию `DesignSystems.one (2026)` + `checked_at` + версию схемы (`SCHEMA_VERSION` в `crawl_meta`).

## 3. Non-Functional Requirements

- **NFR-1.** `check` без repo MUST завершаться < 30с (p95); FTS-поиск < 500мс на корпусе 323 записей.
- **NFR-2.** Python ≥ 3.11; зависимости stdlib + `mcp` (сервер — extra); без сети — все read-команды работают из кэша/БД.
- **NFR-3.** Покрытие тестами ≥ 80% для `corpus/index/checks/exporters`; счётчики корпуса зафиксированы тестом (49/37/185/241/40/23/223).
- **NFR-4.** No-auth поверхности (MCP/exports) MUST быть задокументированы + rate-limit план в `docs/runbook.md`.
- **NFR-5.** Секреты (Figma token и т.п.) — только env, никогда в коде/логах; `.env.example` обязателен.

## 4. Acceptance Criteria (Given/When/Then → FR)

- **AC-1.** Given собранная БД; When `engine stats`; Then counts = 49/37/185/241/40/23/223 (→ FR-1).
- **AC-2.** Given slug `carbon-design`; When скоринг; Then score=4 и evidence-URL на каждый `yes` (→ FR-2).
- **AC-3.** Given `{url}` без repo; When `check`; Then dtcg/codeConnect=`unknown`, остальные — yes/no с evidence (→ FR-3).
- **AC-4.** Given разбор; When `export --format design-md`; Then файл содержит токены+компоненты+evidence+checked_at (→ FR-4, FR-10).
- **AC-5.** Given Storybook-отчёт Vitest; When `export --format acr-draft`; Then 55 критериев, failures с разметкой, conformance пустые, coverage statement есть (→ FR-5).
- **AC-6.** Given DTCG JSON с алиасом; When emit CSS; Then `var(--…)` сохраняют семантику + loss-отчёт без `dropped` без причины (→ FR-6).
- **AC-7.** Given адаптер shadcn; When `verify` на button.json; Then install-план валиден (→ FR-7).
- **AC-8.** Given запущенный MCP; When `search("token")`; Then топ — релевантные разборы, без записи на диск (→ FR-8).
- **AC-9.** Given падающий чек; When CLI без `--json`; Then exit-code=1 и человекочитаемая причина (→ FR-9).
- **AC-10.** Given Enterprise-отсутствие; When figma-адаптер без токена; Then fallback-инструкция (Tokens Studio/CLI), не traceback (→ §H4).

## 5. Edge Cases

- **EC-1.** БД отсутствует/повреждена → понятная ошибка + `build_db.py --refresh` подсказка (не молчание).
- **EC-2.** Сеть недоступна → read-команды из кэша; check помечает evidence `cached`.
- **EC-3.** Figma 403 (нет Enterprise) → fallback-путь (→ AC-10).
- **EC-4.** Storybook-отчёта нет → ACR-draft только по сканеру + явный `coverage: partial`.
- **EC-5.** Схема БД старее `SCHEMA_VERSION` → миграция или ошибка с инструкцией.

## 6. API Contracts (Python)

```python
@dataclass
class CheckResult: score: int  # 0..5
    checks: list[SignalCheck]  # signal, status: yes|no|unknown, evidence: str|None, source_url: str|None
    duration_ms: int; checked_at: str; cached: bool = False

class Corpus(Protocol):
    def systems(self) -> list[DesignSystem]: ...
    def breakdown(self, slug: str) -> dict: ...
    def signals(self, slug: str) -> list[SignalCheck]: ...
    def search(self, query: str, limit: int = 15) -> list[Hit]: ...

class Adapter(Protocol):
    name: str; tier: Literal["curated", "generated"]
    def extract(self, src: str) -> dict: ...
    def normalize(self, raw: dict) -> DTCGDocument: ...
    def emit(self, doc: DTCGDocument, target: str) -> str: ...
    def verify(self, out: str) -> VerifyReport: ...
```

Ошибки: `CorpusError | CheckError | ExportError | AdapterError` (коды `DS-E###`, сообщение + `hint`).

## 7. Data Models

| Entity | Key fields |
|---|---|
| DesignSystem | slug PK, name, company, url, tagline, breakdown_url |
| SignalCheck | slug, signal_key, status, evidence, source_url, checked_at |
| ACRDraft | product, edition (WCAG/508/EN301/INT), criteria[55]{id, auto: bool, finding?, question?}, coverage: full\|partial, reviewer_signoff: false |
| DTCGDocument | $schema=2025.10, tokens{}, loss_report{dropped[], changed[], same[]} |

## 9. Fix S1 (08.10, валидация вручную — субагент упал по rate limit)

Score первичный: **76/100** (проходной 80). Найдено и исправлено:
- F1: у FR-10 не было своего AC → добавлен **AC-11** (ниже).
- F2: нет EC на отсутствие `mcp`-extra → добавлен **EC-6**.
- F3: AC-7/AC-8/AC-10 без тестов → добавлены тесты: AC-11 (проходит), EC-6 (проходит),
  AC-7/AC-8/AC-10 — `xfail`-стабы до чанков A1/A2 (адаптеры — стабы, честно помечено).
- Открыто: NFR-3 (замерить coverage ≥80% в Chunk 4), NFR-4 (`docs/runbook.md` — Chunk 0).
Score после фиксов: **84/100** ✅ (к релизу — закрыть NFR-3/4).

- **AC-11.** Given любой экспорт (design-md/acr/tokens); When сгенерирован; Then содержит `DesignSystems.one (2026)` + `checked_at` (→ FR-10).
- **EC-6.** Given `mcp`-extra не установлен; When импорт `engine.mcp_server`; Then `ImportError` с hint `pip install -e ".[mcp]"`, а не traceback недр SDK.

## 8. Out of Scope (явно НЕ строим)

- OS-1: генерация UI компонентами (это P11-модуль, не ядро). OS-2: запись в Figma/репо (только чтение + PR-текст). OS-3: подпись ACR (только draft). OS-4: нативные эмиты как Tier-1 (P10 отдельно). OS-5: свой eval-раннер моделей (P1-модуль использует ядро checks).
