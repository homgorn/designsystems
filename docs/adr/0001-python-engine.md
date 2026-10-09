# ADR 0001 — Python-движок поверх SQLite-корпуса

- Статус: accepted (08.10.2026)
- Контекст: корпус уже в SQLite (963 КБ, FTS5), скрипты на Python, stdlib достаточно.
- Решение: Python ≥3.11, ядро — stdlib only; `mcp` — extra. CLI — argparse (D3).
- Альтернативы: Node/TS (отклонено: корпус и скиллы команды — Python), Typer (отклонено: лишний dep).
