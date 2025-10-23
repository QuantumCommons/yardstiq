from abc import ABC, abstractmethod
from typing import Any, Dict


class QPU(ABC):
    def __init__(self, config: Dict[str, Any]):
        self.config = config

    @abstractmethod
    def execute(self, circuit: Any, shots: int) -> Dict[str, float]:
        pass
