from dataclasses import dataclass
from dataclasses_json import dataclass_json
from enum import Enum


class ModelSerializationFormat(Enum):
    UNKOWN_SERIALIZATION = 0
    QASM_V1 = 1
    QASM_V2 = 2
    QASM_V3 = 3
    QIR_V1 = 4
    CIRQ_JSON_V1 = 5


@dataclass_json
@dataclass
class ComputationalModel:
    serialization_format: ModelSerializationFormat
    serialization: str

    def to_qiskit_circuit(self) -> "QuantumCircuit":
        from qiskit import qasm3, qasm2, QuantumCircuit

        match = {
            ModelSerializationFormat.QASM_V1: QuantumCircuit.from_qasm_str,
            ModelSerializationFormat.QASM_V2: qasm2.loads,
            ModelSerializationFormat.QASM_V3: qasm3.loads,
        }

        try:
            return match[self.serialization_format](self.serialization)
        except:
            raise Exception(
                "unsupported serialization format:", self.serialization_format
            )

    def to_qsim_circuit(self) -> "Circuit":
        if self.serialization_format in [
            ModelSerializationFormat.QASM_V1,
            ModelSerializationFormat.QASM_V2,
        ]:
            from cirq.contrib.qasm_import import circuit_from_qasm

            return circuit_from_qasm(self.serialization)

        if self.serialization_format in [
            ModelSerializationFormat.CIRQ_JSON_V1,
        ]:
            from cirq import read_json

            return read_json(json_text=self.serialization)

        raise Exception("unsupported serialization format:", self.serialization_format)
