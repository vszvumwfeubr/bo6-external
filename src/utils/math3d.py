"""Small 3D math helpers used by ESP/aimbot plugins."""
from __future__ import annotations

import math
import struct
from typing import Sequence


def world_to_screen(pos: Sequence[float], view_matrix: bytes, size: tuple[int, int]) -> tuple[int, int] | None:
    m = struct.unpack("<16f", view_matrix)
    x, y, z = pos
    clip_x = x * m[0] + y * m[4] + z * m[8] + m[12]
    clip_y = x * m[1] + y * m[5] + z * m[9] + m[13]
    clip_w = x * m[3] + y * m[7] + z * m[11] + m[15]
    if clip_w < 0.01:
        return None
    ndc_x = clip_x / clip_w
    ndc_y = clip_y / clip_w
    w, h = size
    return int((w / 2) * (ndc_x + 1)), int((h / 2) * (1 - ndc_y))


def angle_delta(a: float, b: float) -> float:
    d = math.fmod(a - b + math.pi, math.tau) - math.pi
    return d if d < math.pi else d + math.tau