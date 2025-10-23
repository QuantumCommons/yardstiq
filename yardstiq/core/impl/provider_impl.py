import subprocess
import sys
import json
import importlib.resources

from typing import Dict, Any


def list_knwon_providers() -> Dict[str, Any]:
    """Loads and returns the known provider catalog."""
    try:
        catalog_file = importlib.resources.files("yardstiq").joinpath(
            "data/known_providers.json"
        )
        with open(catalog_file, "r") as f:
            return json.load(f)
    except Exception:
        # Return empty if file not found or ill-formed
        return {}


def _get_package_name_from_catalog(provider_name: str) -> str:
    """Finds the PyPI package name from the provider shortcut name."""
    catalog = list_knwon_providers()

    if provider_name not in catalog:
        raise KeyError(f"Provider '{provider_name}' not found in catalog.")

    return catalog[provider_name]["package_name"]


def add_provider(provider_name: str) -> Dict[str, Any]:
    """
    Installs a provider package via pip.
    Returns a dict with operation status.
    """
    package_name = _get_package_name_from_catalog(provider_name)

    try:
        # Run pip install
        subprocess.check_call(
            [sys.executable, "-m", "pip", "install", package_name],
            stdout=subprocess.DEVNULL,  # Suppress pip output
            stderr=subprocess.PIPE,
        )
        return {"status": "success", "action": "install", "package": package_name}
    except subprocess.CalledProcessError as e:
        raise RuntimeError(
            f"pip install failed for {package_name}: {e.stderr.decode()}"
        )


def remove_provider(provider_name: str) -> Dict[str, Any]:
    """
    Uninstalls a provider package via pip.
    Returns a dict with operation status.
    """
    package_name = _get_package_name_from_catalog(provider_name)

    try:
        # Run pip uninstall
        subprocess.check_call(
            [sys.executable, "-m", "pip", "uninstall", "-y", package_name],
            stdout=subprocess.DEVNULL,  # Suppress pip output
            stderr=subprocess.PIPE,
        )
        return {"status": "success", "action": "remove", "package": package_name}
    except subprocess.CalledProcessError as e:
        raise RuntimeError(
            f"pip uninstall failed for {package_name}: {e.stderr.decode()}"
        )
