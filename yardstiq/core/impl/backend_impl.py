from typing import List

from ..interfaces import BackendProvider, Backend
from ..plugins import PROVIDER_REGISTRY


def list_available_backends() -> List[Backend]:
    """Returns a list of all discoverable QPU names."""
    backends = []

    for name, provider in PROVIDER_REGISTRY.items():
        if isinstance(provider, BackendProvider):
            try:
                for qpu_name in provider.list_backends():
                    backends.append(provider.get_full_name(qpu_name))
            except Exception as e:
                print(
                    f"[Yardstiq] WARNING: Provider '{name}' failed to list backends: {e}"
                )

    return backends
