"""Config loader — merges config/default.yaml with optional local overrides."""
from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parents[2]


def load_config(name: str = "default") -> dict[str, Any]:
    base = yaml.safe_load((ROOT / "config" / f"{name}.yaml").read_text()) or {}
    local = ROOT / "config" / "local.yaml"
    if local.exists():
        base.update(yaml.safe_load(local.read_text()) or {})
    return base