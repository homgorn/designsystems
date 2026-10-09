"""Разовый фикс бэклога: note '22 tools' -> '23 tools' (факт: mcp_tools = 23)."""

import shutil
import sqlite3
from pathlib import Path

DB = Path(__file__).resolve().parent.parent / "db" / "designsystems.db"

shutil.copy(DB, str(DB) + ".bak-22to23")  # бэкап до записи (runbook)
con = sqlite3.connect(DB)
rows = con.execute(
    "SELECT path, note FROM monetization_surfaces WHERE note LIKE '%22 tools%'"
).fetchall()
print("BEFORE:", rows)
con.execute(
    "UPDATE monetization_surfaces SET note = REPLACE(note, '22 tools', '23 tools') "
    "WHERE note LIKE '%22 tools%'"
)
con.commit()
print("AFTER:", con.execute(
    "SELECT path, note FROM monetization_surfaces WHERE path='/api/mcp'"
).fetchall())
print("mcp_tools count:", con.execute("SELECT COUNT(*) FROM mcp_tools").fetchone()[0])
con.close()
