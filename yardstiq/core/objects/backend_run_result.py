from typing import Dict

from dataclasses import dataclass
from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class BackendRunResult:
    results: Dict[str, float]
    shots: int

    @classmethod
    def from_qiskit_result(cls) -> "BenchmarkRunResult":
        pass
