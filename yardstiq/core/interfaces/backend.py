from abc import ABC, abstractmethod
from enum import Enum

from ..objects import BackendRunResult, ComputationalModel


class BackendAvailability(Enum):
    AVAILABLE = "online"
    OFFLINE = "offline"
    MAINTENANCE = "maintenance"


class Backend(ABC):
    def __init__(self, provider):
        self._provider = provider

    @abstractmethod
    def run(self, model: ComputationalModel, shots: int, **kwargs) -> BackendRunResult:
        pass

    def full_name(self) -> str:
        return self._provider.get_full_name(self.name)

    @abstractmethod
    @property
    def name(self) -> str:
        pass

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
