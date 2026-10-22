"""ESP overlay plugin — draws player boxes and names via the overlay service."""
from __future__ import annotations

import logging

from src.contracts.plugin_api import BasePlugin, PluginContext
from src.utils.math3d import world_to_screen

log = logging.getLogger("bo6.plugin.esp")


class ESPPlugin(BasePlugin):
    name = "esp"
    enabled = False

    def on_load(self, ctx: PluginContext) -> None:
        super().on_load(ctx)
        self._max_dist = ctx.config.get("esp_max_distance", 250.0)

    def on_tick(self, ctx: PluginContext) -> None:
        if ctx.memory is None or ctx.overlay is None:
            return
        vm = ctx.memory.read(0x1A3F9010, 64)
        for entity in ctx.process.entities() if ctx.process else []:
            pos = entity.position
            screen = world_to_screen(pos, vm, ctx.overlay.size)
            if screen is None:
                continue
            ctx.overlay.draw_box(screen, entity.health)