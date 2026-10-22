from src.host.registry import PluginRegistry


def test_registry_discovers_builtin_plugins():
    reg = PluginRegistry()
    names = reg.available()
    assert "esp" in names
    assert "aimbot" in names
    assert "radar" in names


def test_registry_resolves_known_plugin():
    reg = PluginRegistry()
    cls = reg.resolve("esp")
    assert cls.name == "esp"
    assert cls.enabled is False
</｜｜DSML｜｜ parameter>