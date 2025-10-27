from abc import ABC, abstractmethod
from typing import List

from .dataset import Dataset
from .benchmark import Benchmark
from .backend import Backend


class Provider(ABC):
    """
    Base interface for all resource providers.
    A provider is a factory for resources (backends, Datasets, etc.).
    """

    def __init__(self, name: str = ""):
        self.__name = name

    def get_full_name(self, resource_name: str) -> str:
        """Helper to create a namespaced ID, e.g., 'scaleway/quandela'"""
        return f"{self.__name}/{resource_name}"


class BackendProvider(Provider):
    """Interface for a provider that can discover and instantiate backends."""

    @abstractmethod
    def list_backends(self) -> List[Backend]:
        """
        Returns a list of available backend names this provider offers.
        e.g., ["quandela-ascella", "pasqal-fresnel"]
        """
        pass

    @abstractmethod
    def get_backend(self, name: str) -> Backend:
        """
        Returns an instantiated backend object for the given name.
        'name' is one of the names from list_backends().
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
