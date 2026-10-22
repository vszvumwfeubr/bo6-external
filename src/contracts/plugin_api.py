"""Shared contract every plugin must implement."""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Protocol, runtime_checkable


@dataclass
class PluginContext:
    """Handed to every plugin on load/tick. Holds shared services."""
    process: Any = None
    memory: Any = None
    overlay: Any = None
    config: dict[str, Any] = field(default_factory=dict)


@runtime_checkable
class Plugin(Protocol):
    name: str = ""
    enabled: bool = True

    def on_load(self, ctx: PluginContext) -> None: ...
    def on_tick(self, ctx: PluginContext) -> None: ...
    def on_unload(self) -> None: ...


class BasePlugin:
    name = "base"
    enabled = True

    def on_load(self, ctx: PluginContext) -> None:
        self.ctx = ctx

    def on_tick(self, ctx: PluginContext) -> None:
        pass

    def on_unload(self) -> None:
        pass