from abc import ABC, abstractmethod
from typing import Any, Dict


class QPU(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def execute(self, circuit: Any, shots: int) -> Dict[str, float]:
        pass
