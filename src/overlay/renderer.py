"""Transparent click-through overlay renderer (pygame + Win32)."""
from __future__ import annotations

import logging

log = logging.getLogger("bo6.overlay")


class OverlayRenderer:
    def __init__(self, width: int = 1920, height: int = 1080) -> None:
        self.size = (width, height)
        self._surface = None
        self._lines: list[tuple] = []

    def init(self) -> None:
        import pygame  # type: ignore
        pygame.init()
        self._surface = pygame.display.set_mode(self.size, pygame.NOFRAME)
        log.info("overlay surface %sx%s", *self.size)

    def begin_frame(self) -> None:
        self._lines.clear()

    def draw_box(self, pt: tuple[int, int], health: float) -> None:
        self._lines.append(("box", pt, health))

    def draw_radar_dot(self, x: float, y: float, friendly: bool) -> None:
        self._lines.append(("dot", (x, y), friendly))

    def move_mouse(self, dx: float, dy: float) -> None:
        # delegated to input backend in full build
        pass

    def present(self) -> None:
        if self._surface is None:
            return
        import pygame  # type: ignore
        self._surface.fill((0, 0, 0, 0))
        pygame.display.flip()