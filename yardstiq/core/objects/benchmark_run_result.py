from dataclasses import dataclass
from dataclasses_json import dataclass_json
from typing import Dict, Any


@dataclass_json
@dataclass
class BenchmarkRunResult:
    benchmark_name: str
    qpu_name: str
    scores: Dict[str, float]

    @classmethod
    def from_qiskit_result(cls) -> "BenchmarkRunResult":
        pass
