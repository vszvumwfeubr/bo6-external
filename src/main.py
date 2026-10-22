"""bo6-external entrypoint. Educational use only."""
from __future__ import annotations

import argparse
import logging

from src.host.plugin_host import PluginHost
from src.host.registry import PluginRegistry
from src.contracts.plugin_api import PluginContext
from src.memory.process import ProcessHandle
from src.memory.reader import MemoryReader
from src.overlay.renderer import OverlayRenderer
from src.utils.config import load_config


def build_ctx(cfg: dict) -> PluginContext:
    proc = ProcessHandle(cfg["process"]["name"])
    proc.attach()
    reader = MemoryReader(proc.handle) if proc.handle else None
    overlay = OverlayRenderer(cfg["overlay"]["width"], cfg["overlay"]["height"])
    return PluginContext(process=proc, memory=reader, overlay=overlay, config=cfg)


def main() -> None:
    parser = argparse.ArgumentParser(description="bo6-external (educational)")
    parser.add_argument("--config", default="default")
    parser.add_argument("--plugins", default="")
    args = parser.parse_args()

    cfg = load_config(args.config)
    logging.basicConfig(level=cfg["host"]["log_level"])

    registry = PluginRegistry()
    ctx = build_ctx(cfg)
    host = PluginHost(registry, ctx)
    names = [n.strip() for n in args.plugins.split(",") if n.strip()] or None
    host.load(names)
    try:
        host.run(fps=cfg["host"]["fps"])
    except KeyboardInterrupt:
        pass
    finally:
        host.stop()


if __name__ == "__main__":
    main()