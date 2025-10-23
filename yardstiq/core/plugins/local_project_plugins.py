import toml

from pathlib import Path
from .local_manual_plugins import load_local_plugin


def find_config_file() -> Path | None:
    current_dir = Path.cwd()
    for parent in [current_dir] + list(current_dir.parents):
        config_path = parent / "pyproject.toml"
        if config_path.exists():
            return config_path
    return None


def load_project_plugins():
    """
    Loads local plugins declared in a pyproject.toml [tool.yardstiq] section.
    """
    config_file = find_config_file()
    if not config_file:
        return

    try:
        config = toml.load(config_file)
        plugin_paths = (
            config.get("tool", {}).get("yardstiq", {}).get("local_plugins", [])
        )

        if not plugin_paths:
            return

        print(f"[Yardstiq] Loading project plugins from {config_file.name}...")
        base_dir = config_file.parent

        for rel_path_str in plugin_paths:
            abs_path = base_dir / rel_path_str
            # Re-uses the same logic as --load
            load_local_plugin(abs_path)

    except Exception as e:
        print(f"[Yardstiq] WARNING: Failed to load from pyproject.toml: {e}")
