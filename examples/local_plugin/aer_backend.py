from yardstiq.core import backend, ComputationalModel, BackendRunResult

from qiskit import transpile
from qiskit_aer import AerSimulator


@backend("aer")
class AerBackend:
    def run(self, model: ComputationalModel) -> BackendRunResult:
        aer_simulator = AerSimulator(method="statevector", device="CPU")

        circuit = model.to_qiskit_circuit()

        transpiled_circuit = transpile(circuit, aer_simulator)

        result = aer_simulator.run(transpiled_circuit).result()

        return BackendRunResult.from_qiskit_result(result)
