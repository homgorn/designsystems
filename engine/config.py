"""Конфиг движка: пути + env-переопределения. Секреты — только env (см. .env.example)."""

from __future__ import annotations

import os
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def db_path() -> Path:
    return Path(os.environ.get("DS_DB", ROOT / "db" / "designsystems.db"))


def figma_token() -> str | None:
    return os.environ.get("FIGMA_TOKEN")
