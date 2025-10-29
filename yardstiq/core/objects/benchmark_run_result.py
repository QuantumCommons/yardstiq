from dataclasses import dataclass
from dataclasses_json import dataclass_json
from typing import Dict, Any


@dataclass_json
@dataclass
class BenchmarkRunResult:
    scores: Dict[str, float]
