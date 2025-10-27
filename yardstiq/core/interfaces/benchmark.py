from abc import ABC, abstractmethod
from typing import Any, Dict, Optional

from .dataset import Dataset


class Benchmark(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def build_circuit(self, dataset: Optional[Dataset]) -> Any:
        pass

    @abstractmethod
    def score(self, results: Dict[str, float]) -> Dict[str, Any]:
        pass
