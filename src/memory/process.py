"""Locate and attach to the Black Ops 6 process (educational)."""
from __future__ import annotations

import logging

log = logging.getLogger("bo6.process")

PROCESS_NAME = "cod.exe"


class ProcessHandle:
    def __init__(self, name: str = PROCESS_NAME) -> None:
        self.name = name
        self.pid: int | None = None
        self.handle = None

    def attach(self) -> bool:
        try:
            import pymem  # type: ignore
        except ImportError:
            log.error("pymem is required for process attach")
            return False
        try:
            self.handle = pymem.Pymem(self.name)
            self.pid = self.handle.process_id
            log.info("attached to %s (pid=%s)", self.name, self.pid)
            return True
        except Exception as exc:
            log.warning("could not attach to %s: %s", self.name, exc)
            return False

    @property
    def module_base(self) -> int:
        if self.handle is None:
            raise RuntimeError("not attached")
        return self.handle.base_address

    def detach(self) -> None:
        self.handle = None
        self.pid = None