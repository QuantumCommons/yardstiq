from typing import List

from ..interfaces.provider import DatasetProvider
from ..plugins import PROVIDER_REGISTRY


def list_available_datasets() -> List[str]:
    all_datasets = []
    for name, provider_instance in PROVIDER_REGISTRY.items():
        if isinstance(provider_instance, DatasetProvider):
            try:
                for ds_name in provider_instance.list_datasets():
                    all_datasets.append(provider_instance.get_full_name(ds_name))
            except Exception as e:
                print(
                    f"[Yardstiq] WARNING: Provider '{name}' failed to list datasets: {e}"
                )
    return all_datasets
