"""Plugin registry: maps short names to plugin classes."""
from __future__ import annotations

import importlib
import pkgutil
from typing import Type

from src.contracts.plugin_api import Plugin


class PluginRegistry:
    def __init__(self, package: str = "src.plugins") -> None:
        self._package = package
        self._cache: dict[str, Type[Plugin]] = {}

    def discover(self) -> None:
        pkg = importlib.import_module(self._package)
        for _, modname, _ in pkgutil.iter_modules(pkg.__path__):
            if modname.startswith("_"):
                continue
            module = importlib.import_module(f"{self._package}.{modname}")
            for attr in dir(module):
                obj = getattr(module, attr)
                if isinstance(obj, type) and issubclass(obj, Plugin) and obj is not Plugin:
                    self._cache[obj.name or modname] = obj

    def available(self) -> list[str]:
        if not self._cache:
            self.discover()
        return sorted(self._cache)

    def resolve(self, name: str) -> Type[Plugin]:
        if not self._cache:
            self.discover()
        try:
            return self._cache[name]
        except KeyError as exc:
            raise LookupError(f"plugin {name!r} not registered") from exc