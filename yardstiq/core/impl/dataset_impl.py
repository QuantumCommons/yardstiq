from typing import List

from ..interfaces import DatasetProvider, Dataset
from ..plugins import PROVIDER_REGISTRY


def list_available_datasets() -> List[Dataset]:
    datasets = []

    for name, provider in PROVIDER_REGISTRY.items():
        if isinstance(provider, DatasetProvider):
            try:
                for ds_name in provider.list_datasets():
                    datasets.append(provider.get_full_name(ds_name))
            except Exception as e:
                print(
                    f"[Yardstiq] WARNING: Provider '{name}' failed to list datasets: {e}"
                )

    return datasets
