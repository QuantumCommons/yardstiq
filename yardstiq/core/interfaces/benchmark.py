from abc import ABC, abstractmethod
from typing import Any, Dict


class Benchmark(ABC):
    def __init__(self, config: Dict[str, Any]):
        self.config = config

    @abstractmethod
    def build_circuit(self, dataset: Any) -> Any:
        pass

    @abstractmethod
    def score(self, results: Dict[str, float]) -> Dict[str, Any]:
        pass
