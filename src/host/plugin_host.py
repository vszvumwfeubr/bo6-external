"""Core plugin host. Loads plugins from src/plugins and drives their ticks."""
from __future__ import annotations

import logging
import time
from typing import Iterable

from src.contracts.plugin_api import Plugin, PluginContext
from src.host.registry import PluginRegistry

log = logging.getLogger("bo6.host")


class PluginHost:
    def __init__(self, registry: PluginRegistry, ctx: PluginContext) -> None:
        self._registry = registry
        self._ctx = ctx
        self._plugins: list[Plugin] = []
        self._running = False

    def load(self, names: Iterable[str] | None = None) -> None:
        for name in names or self._registry.available():
            cls = self._registry.resolve(name)
            try:
                plugin = cls()
                plugin.on_load(self._ctx)
                self._plugins.append(plugin)
                log.info("loaded plugin %s", name)
            except Exception:
                log.exception("failed to load plugin %s", name)

    def tick(self) -> None:
        for plugin in self._plugins:
            if not plugin.enabled:
                continue
            try:
                plugin.on_tick(self._ctx)
            except Exception:
                log.exception("plugin %s raised during tick", plugin.name)

    def run(self, fps: int = 60) -> None:
        self._running = True
        frame = 1.0 / fps
        while self._running:
            start = time.perf_counter()
            self.tick()
            elapsed = time.perf_counter() - start
            if elapsed < frame:
                time.sleep(frame - elapsed)

    def stop(self) -> None:
        self._running = False
        for plugin in reversed(self._plugins):
            try:
                plugin.on_unload()
            except Exception:
                log.exception("plugin %s failed to unload", plugin.name)