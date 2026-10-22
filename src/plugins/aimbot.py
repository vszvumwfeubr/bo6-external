"""Aimbot plugin — educational demonstration of smoothing + FOV gating."""
from __future__ import annotations

import math

from src.contracts.plugin_api import BasePlugin, PluginContext


class AimbotPlugin(BasePlugin):
    name = "aimbot"
    enabled = False

    def on_load(self, ctx: PluginContext) -> None:
        super().on_load(ctx)
        self.fov = ctx.config.get("aim_fov", 45.0)
        self.smoothing = ctx.config.get("aim_smoothing", 8.0)
        self.key = ctx.config.get("aim_key", "shift")

    def on_tick(self, ctx: PluginContext) -> None:
        if not self.enabled or ctx.memory is None:
            return
        target = self._best_target(ctx)
        if target is None:
            return
        dx, dy = target
        dist = math.hypot(dx, dy)
        if dist > self.fov:
            return
        step_x = dx / self.smoothing
        step_y = dy / self.smoothing
        ctx.overlay.move_mouse(step_x, step_y)

    def _best_target(self, ctx: PluginContext) -> tuple[float, float] | None:
        # stub: real implementation reads entity list + view matrix
        return None