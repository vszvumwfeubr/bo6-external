"""Load build-specific offset tables from JSON."""
from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path

OFFSET_DIR = Path(__file__).parent / "tables"


@dataclass(frozen=True)
class OffsetTable:
    build: str
    game_version: str
    entity_list: int
    local_player: int
    view_matrix: int
    bone_matrix: int


def load_offsets(build: str) -> OffsetTable:
    path = OFFSET_DIR / f"{build}.json"
    if not path.exists():
        raise FileNotFoundError(f"no offset table for build {build!r}")
    data = json.loads(path.read_text())
    return OffsetTable(
        build=data["build"],
        game_version=data.get("game_version", "unknown"),
        entity_list=data["entity_list"],
        local_player=data["local_player"],
        view_matrix=data["view_matrix"],
        bone_matrix=data["bone_matrix"],
    )