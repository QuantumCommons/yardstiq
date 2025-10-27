from abc import ABC, abstractmethod
from typing import Any, Dict


class Dataset(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def load(self) -> Any:
        pass
