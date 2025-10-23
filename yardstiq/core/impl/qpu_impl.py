from typing import List

from ..interfaces.provider import QpuProvider
from ..plugins import PROVIDER_REGISTRY


def list_available_qpus() -> List[str]:
    """Returns a list of all discoverable QPU names."""
    all_qpus = []

    for name, provider_instance in PROVIDER_REGISTRY.items():
        if isinstance(provider_instance, QpuProvider):
            try:
                for qpu_name in provider_instance.list_qpus():
                    all_qpus.append(provider_instance.get_full_name(qpu_name))
            except Exception as e:
                print(f"[Yardstiq] WARNING: Provider '{name}' failed to list QPUs: {e}")

    return all_qpus
