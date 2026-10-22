"""Radar plugin — minimap-style top-down view of nearby players."""
from __future__ import annotations

from src.contracts.plugin_api import BasePlugin, PluginContext


class RadarPlugin(BasePlugin):
    name = "radar"
    enabled = False

    def on_load(self, ctx: PluginContext) -> None:
        super().on_load(ctx)
        self.radius = ctx.config.get("radar_radius", 60.0)

    def on_tick(self, ctx: PluginContext) -> None:
        if ctx.overlay is None or ctx.process is None:
            return
        local = ctx.process.local_player()
        if local is None:
            return
        for ent in ctx.process.entities():
            rel = ent.position - local.position
            if abs(rel.x) > self.radius or abs(rel.y) > self.radius:
                continue
            ctx.overlay.draw_radar_dot(rel.x, rel.y, ent.team == local.team)