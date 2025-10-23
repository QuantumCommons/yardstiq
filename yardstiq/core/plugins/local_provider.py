from typing import Dict, Type

from ..interfaces import (
    QPU,
    Benchmark,
    Dataset,
    QpuProvider,
    BenchmarkProvider,
    DatasetProvider,
)


class LocalProvider(QpuProvider, BenchmarkProvider, DatasetProvider):
    """
    A built-in singleton provider that holds all implementations
    loaded from local files (via --load or pyproject.toml).
    """

    def __init__(self):
        super().__init__()
        self.name = "local"

        # Internal registries for locally-defined classes
        self.qpu_registry: Dict[str, Type[QPU]] = {}
        self.benchmark_registry: Dict[str, Type[Benchmark]] = {}
        self.dataset_registry: Dict[str, Type[Dataset]] = {}

    # --- QpuProvider Implementation ---
    def list_qpus(self) -> list[str]:
        return list(self.qpu_registry.keys())

    def get_qpu(self, qpu_name: str, config: Dict) -> QPU:
        try:
            QpuCls = self.qpu_registry[qpu_name]
            return QpuCls(config)
        except KeyError:
            raise KeyError(f"Local QPU '{qpu_name}' not found.")

    # --- BenchmarkProvider Implementation ---
    def list_benchmarks(self) -> list[str]:
        return list(self.benchmark_registry.keys())

    def get_benchmark(self, benchmark_name: str, config: Dict) -> Benchmark:
        try:
            BenchmarkCls = self.benchmark_registry[benchmark_name]
            return BenchmarkCls(config)
        except KeyError:
            raise KeyError(f"Local benchmark '{benchmark_name}' not found.")

    # --- DatasetProvider Implementation ---
    def list_datasets(self) -> list[str]:
        return list(self.dataset_registry.keys())

    def get_dataset(self, dataset_name: str, config: Dict) -> Dataset:
        try:
            DatasetCls = self.dataset_registry[dataset_name]
            return DatasetCls(config)
        except KeyError:
            raise KeyError(f"Local dataset '{dataset_name}' not found.")


local_provider_instance = LocalProvider()
