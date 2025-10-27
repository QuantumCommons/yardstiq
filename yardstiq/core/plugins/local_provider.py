from typing import Dict, Type, List

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
        super().__init__(name="local")

        # Internal registries for locally-defined classes
        self.__qpus: Dict[str, Type[QPU]] = {}
        self.__benchmarks: Dict[str, Type[Benchmark]] = {}
        self.__datasets: Dict[str, Type[Dataset]] = {}

    def add_qpu(self, qpu: QPU, name: str):
        self.__qpus[name] = qpu

    def list_qpus(self) -> List[QPU]:
        return list(self.__qpus.keys())

    def get_qpu(self, name: str) -> QPU:
        try:
            return self.__qpus[name]
        except KeyError:
            raise KeyError(f"Local QPU '{name}' not found.")

    def add_benchmark(self, benchmark: Benchmark, name: str):
        self.__benchmarks[name] = benchmark

    def list_benchmarks(self) -> List[str]:
        return list(self.__benchmarks.keys())

    def get_benchmark(self, name: str) -> Benchmark:
        try:
            return self.__benchmarks[name]
        except KeyError:
            raise KeyError(f"Local benchmark '{name}' not found.")

    def add_dataset(self, dataset: Dataset, name: str):
        self.__datasets[name] = dataset

    def list_datasets(self) -> List[str]:
        return list(self.__datasets.keys())

    def get_dataset(self, name: str) -> Dataset:
        try:
            return self.__datasets[name]
        except KeyError:
            raise KeyError(f"Local dataset '{name}' not found.")
