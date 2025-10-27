from dataclasses import dataclass
from dataclasses_json import dataclass_json
from enum import Enum


class ModelSerializationFormat(Enum):
    UNKOWN_CIRCUIT_SERIALIZATION = 0
    QASM_V1 = 1
    QASM_V2 = 2
    QASM_V3 = 3
    QIR_V1 = 4


@dataclass_json
@dataclass
class ComputationalModel:
    model_format: ModelSerializationFormat
    model_serialization: str
