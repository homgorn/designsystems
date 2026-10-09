# 07. LLM-корпус и БД: как пользоваться

## Файлы

- `db/designsystems.db` — SQLite (~963 КБ), WAL. Пересборка: `python scripts/build_db.py` (из кэша, без сети) / `--refresh` (сеть) / `--skip-breakdowns`.
- `scripts/query.py` — CLI: `stats|top [N]|signals|system <slug>|search <terms>|glossary [t]|money|sections|links <slug>`.
- `research/raw/` — вербатим API/HTML (11 файлов + 49 разборов).

## Схема (16 таблиц)

`design_systems(49)` — slug PK, name, company, url, tagline, breakdown_url, rich_breakdown, in_gallery · `breakdowns(49)` — verbatim JSON · `breakdown_links(241)` — kind∈{docs,repo,figma,npm,blog,social,pdf,other} · `ai_ready_systems(37)` — score 0–5, checked_at, notes · `ai_ready_signals(185)` — signal∈{mcp,llmsTxt,dtcg,registry,codeConnect} × status∈{yes,no,unknown,n/a} + evidence/source/method · `glossary(40)` · `registry_items(4)` · `mcp_server(1)+mcp_tools(23)+mcp_prompts(3)+mcp_resources(5)` · `site_urls(223)` + section · `gallery_only(76)` · `monetization_surfaces(17)` · `source_files(10)` + sha · `crawl_meta` · `corpus_fts(323)` — FTS5 (porter unicode61), entity∈{design_system,breakdown,ai_signal,glossary}.

## Примеры запросов

```sql
-- топ AI-ready
SELECT name,company,score FROM ai_ready_systems ORDER BY score DESC LIMIT 10;
-- кто без MCP
SELECT s.name FROM ai_ready_systems s JOIN ai_ready_signals g
  ON g.slug=s.slug WHERE g.signal_key='mcp' AND g.status='no';
-- FTS: всё про токены миграции
SELECT entity,entity_id,title FROM corpus_fts WHERE corpus_fts MATCH 'token migration';
-- ссылки одного разбора
SELECT kind,url FROM breakdown_links WHERE slug='carbon-design';
-- точки монетизации
SELECT kind,path,title FROM monetization_surfaces ORDER BY kind;
```

## Правила цитирования для следующих агентов

1. Факт из БД = уверенность 9/10, ссылка `db:<таблица>/<slug>`.
2. Цифры трафика/выручки без источника = максимум 5/10, метка `[оценка]`.
3. Не выдумывать: нет данных → `[нет данных]` + куда смотреть (`research/04-fetch-log.md` §«Не скачано»).
4. Расхождение 11 000 vs 300–2 000 не замалчивать — приводить оба числа.
5. CC BY 4.0: при републикации индекса — атрибуция `DesignSystems.one (2026). Agent-Ready Design Systems Index. https://www.designsystems.one/ai-ready/systems`.
