from abc import ABC, abstractmethod
from typing import Any, Dict, Optional

from .dataset import Dataset

from ..objects import ComputationalModel, BenchmarkRunResult, BackendRunResult


class Benchmark(ABC):
    def __init__(self, provider: "Provider"):
        self._provider = provider

    @abstractmethod
    def build_model(self, dataset: Optional[Dataset]) -> ComputationalModel:
        pass

    @abstractmethod
    def score(self, backend_run_results: BackendRunResult) -> BenchmarkRunResult:
        pass
