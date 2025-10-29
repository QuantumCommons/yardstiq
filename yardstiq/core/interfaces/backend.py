from abc import ABC, abstractmethod
from enum import Enum

from ..objects import BackendRunResult, ComputationalModel


class BackendAvailability(Enum):
    UNKNOWN_AVAILABILITY = 0
    AVAILABLE = 1
    UNAVAILABLE = 2
    MAINTENANCE = 3


class Backend(ABC):
    def __init__(self, provider, name: str, **kwargs):
        self.__provider = provider
        self.__name = name
        self.__additional_properties = kwargs

    def __enter__(self):
        self.allocate(self.__additional_properties)

        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> bool:
        self.deallocate()
        return False

    @abstractmethod
    def allocate(**kwargs) -> None:
        pass

    @abstractmethod
    def deallocate() -> None:
        pass

    @abstractmethod
    def run(self, model: ComputationalModel, shots: int, **kwargs) -> BackendRunResult:
        pass

    @property
    def full_name(self) -> str:
        return self.__provider.get_full_name(self.name)

    @property
    def name(self) -> str:
        return self.__name

    @abstractmethod
    @property
    def max_qubit_count(self) -> int:
        pass

    @abstractmethod
    @property
    def max_shots_per_run(self) -> int:
        pass

    @abstractmethod
    @property
    def availability(self) -> BackendAvailability:
        pass
