from importlib.metadata import entry_points

PLUGIN_ENTRY_POINT_GROUP = "yardstiq.plugins"


def load_installed_plugins():
    """
    Discovers and loads all installed plugins via entry points.
    The decorators (@provider) in the loaded files will register themselves.
    """
    print("[Yardstiq] Loading installed plugins (entry_points)...")
    try:
        discovered_entry_points = entry_points(group=PLUGIN_ENTRY_POINT_GROUP)
    except Exception as e:
        print(f"[Yardstiq] Error reading entry points: {e}")
        return

    for ep in discovered_entry_points:
        try:
            # ep.load() simply imports the module, triggering its decorators
            plugin_module = ep.load()
            print(f"[Yardstiq] Installed plugin '{ep.name}' loaded.")
        except Exception as e:
            print(f"[Yardstiq] WARNING: Failed to load plugin '{ep.name}': {e}")
