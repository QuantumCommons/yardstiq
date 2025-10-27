from abc import ABC, abstractmethod
from typing import List

from .dataset import Dataset
from .benchmark import Benchmark
from .qpu import QPU


class Provider(ABC):
    """
    Base interface for all resource providers.
    A provider is a factory for resources (QPUs, Datasets, etc.).
    """

    def __init__(self, name: str = ""):
        self.__name = name

    def get_full_name(self, resource_name: str) -> str:
        """Helper to create a namespaced ID, e.g., 'scaleway/quandela'"""
        return f"{self.__name}/{resource_name}"


class QpuProvider(Provider):
    """Interface for a provider that can discover and instantiate QPUs."""

    @abstractmethod
    def list_qpus(self) -> List[QPU]:
        """
        Returns a list of available QPU names this provider offers.
        e.g., ["quandela-ascella", "pasqal-fresnel"]
        """
        pass

    @abstractmethod
    def get_qpu(self, name: str) -> QPU:
        """
        Returns an instantiated QPU object for the given name.
        'qpu_name' is one of the names from list_qpus().
        """
        pass


class DatasetProvider(Provider):
    """Interface for a provider that can discover and instantiate Datasets."""

    @abstractmethod
    def list_datasets(self) -> List[Dataset]:
        """
        Returns a list of available dataset names.
        e.g., ["h2-molecule", "max-cut-graph-1"]
        """
        pass

    @abstractmethod
    def get_dataset(self, name: str) -> Dataset:
        """
        Returns an instantiated Dataset object for the given name.
        """
        pass


class BenchmarkProvider(Provider):
    """Interface for a provider that can discover and instantiate Benchmarks."""

    @abstractmethod
    def list_benchmarks(self) -> List[Benchmark]:
        """Returns a list of available benchmark names."""
        pass

    @abstractmethod
    def get_benchmark(self, name: str) -> Benchmark:
        """Returns an instantiated Benchmark object for the given name."""
        pass
