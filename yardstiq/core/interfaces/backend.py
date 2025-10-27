from abc import ABC, abstractmethod
from typing import Any, Dict, List, overload

from ..objects import BackendRunResult, ComputationalModel


class Backend(ABC):
    def __init__(self, provider):
        self._provider = provider

    @abstractmethod
    def run(self, model: ComputationalModel, shots: int, **kwargs) -> BackendRunResult:
        pass
