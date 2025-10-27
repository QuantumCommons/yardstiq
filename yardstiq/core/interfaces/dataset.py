from abc import ABC, abstractmethod
from typing import Any, Dict

from ..objects import ComputationalModel


class Dataset(ABC):
    def __init__(self, provider):
        self._provider = provider

    @abstractmethod
    def load(self, **kwargs) -> ComputationalModel:
        pass
