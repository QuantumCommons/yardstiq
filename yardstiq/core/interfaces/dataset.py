from abc import ABC, abstractmethod
from typing import Any, Dict


class Dataset(ABC):
    def __init__(self, config: Dict[str, Any]):
        self.config = config

    @abstractmethod
    def load(self) -> Any:
        pass
