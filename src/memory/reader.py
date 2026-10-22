"""Thin wrapper around pymem for typed reads."""
from __future__ import annotations

import struct
from typing import Any


class MemoryReader:
    def __init__(self, handle: Any) -> None:
        self._h = handle

    def read(self, address: int, size: int) -> bytes:
        return self._h.read_bytes(address, size)

    def read_int(self, address: int) -> int:
        return struct.unpack("<i", self.read(address, 4))[0]

    def read_float(self, address: int) -> float:
        return struct.unpack("<f", self.read(address, 4))[0]

    def read_vec3(self, address: int) -> tuple[float, float, float]:
        return struct.unpack("<fff", self.read(address, 12))

    def read_pointer(self, address: int) -> int:
        return struct.unpack("<Q", self.read(address, 8))[0]

    def read_chain(self, base: int, offsets: list[int]) -> int:
        addr = base
        for off in offsets[:-1]:
            addr = self.read_pointer(addr + off)
        return addr + offsets[-1]