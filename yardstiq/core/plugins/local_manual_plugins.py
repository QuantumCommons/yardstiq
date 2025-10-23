import importlib.util
import sys

from pathlib import Path


def load_local_plugin(module_path: Path):
    """
    Loads a single Python module from a local file path.
    The decorators (@qpu, @benchmark) in the file will register themselves.
    """
    try:
        # ... (logique de chargement de module inchangée) ...
        module_path = module_path.resolve()
        if not module_path.exists():
            print(f"[Yardstiq] ERROR: Local file '{module_path}' not found.")
            return

        module_name = module_path.stem
        spec = importlib.util.spec_from_file_location(module_name, module_path)
        if spec is None:
            raise ImportError(f"Could not create spec for {module_path}")

        module = importlib.util.module_from_spec(spec)
        sys.modules[module_name] = module

        # exec_module triggers the decorators
        spec.loader.exec_module(module)

        print(f"[Yardstiq] Local plugin file '{module_path.name}' loaded.")

    except Exception as e:
        print(f"[Yardstiq] WARNING: Failed to load local plugin '{module_path}': {e}")
