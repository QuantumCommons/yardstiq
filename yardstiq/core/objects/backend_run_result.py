from dataclasses import dataclass
from dataclasses_json import dataclass_json
from typing import Dict


@dataclass_json
@dataclass
class BackendRunResult:
    backend_name: str
    results: Dict[str, float]
    shots: int
