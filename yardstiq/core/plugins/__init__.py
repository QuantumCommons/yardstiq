from typing import Dict, Type, Callable, List
from pathlib import Path

from ..interfaces import Provider, QPU, Benchmark, Dataset

from .local_provider import local_provider_instance
from .installed_plugins import load_installed_plugins
from .local_project_plugins import load_project_plugins
from .local_manual_plugins import load_local_plugin

PROVIDER_REGISTRY: Dict[str, Provider] = {"local": local_provider_instance}

_plugins_loaded = False


def provider(name: str) -> Callable:
    """
    DECORATOR (for packages): Registers a new Provider class.
    Used by external packages like 'yardstiq-scaleway-qpu'.
    """

    def decorator(cls: Type[Provider]) -> Type[Provider]:
        if not issubclass(cls, Provider):
            raise TypeError(f"Class {cls.__name__} must inherit from Provider")

        if name in PROVIDER_REGISTRY:
            print(f"[Yardstiq] WARNING: Provider '{name}' is being redefined.")

        try:
            # Instancie le provider et l'ajoute au registre
            instance = cls()
            instance.name = name
            PROVIDER_REGISTRY[name] = instance
        except Exception as e:
            print(f"[Yardstiq] WARNING: Failed to instantiate provider '{name}': {e}")

        return cls

    return decorator


def qpu(name: str) -> Callable:
    """
    DECORATOR (for local files): Registers a QPU class
    with the implicit 'local' provider.
    """

    def decorator(cls: Type[QPU]) -> Type[QPU]:
        if not issubclass(cls, QPU):
            raise TypeError(f"Class {cls.__name__} must inherit from QPU")

        local_provider_instance.qpu_registry[name] = cls
        return cls

    return decorator


def benchmark(name: str) -> Callable:
    """
    DECORATOR (for local files): Registers a Benchmark class
    with the implicit 'local' provider.
    """

    def decorator(cls: Type[Benchmark]) -> Type[Benchmark]:
        if not issubclass(cls, Benchmark):
            raise TypeError(f"Class {cls.__name__} must inherit from Benchmark")

        local_provider_instance.benchmark_registry[name] = cls
        return cls

    return decorator


def dataset(name: str) -> Callable:
    """
    DECORATOR (for local files): Registers a Dataset class
    with the implicit 'local' provider.
    """

    def decorator(cls: Type[Dataset]) -> Type[Dataset]:
        if not issubclass(cls, Dataset):
            raise TypeError(f"Class {cls.__name__} must inherit from Dataset")

        local_provider_instance.dataset_registry[name] = cls
        return cls

    return decorator


def load_all_plugins(local_files: List[Path] = None):
    """
    Orchestrates loading all plugins.
    This function simply executes the plugin files; the decorators
    do the work of registering themselves.
    """
    global _plugins_loaded
    if _plugins_loaded:
        return

    print("[Yardstiq] Initializing and loading provider plugins...")

    load_installed_plugins()

    load_project_plugins()

    if local_files:
        print(f"[Yardstiq] Loading {len(local_files)} local plugin(s) via --load...")

        for file_path in local_files:
            load_local_plugin(file_path)

    _plugins_loaded = True
