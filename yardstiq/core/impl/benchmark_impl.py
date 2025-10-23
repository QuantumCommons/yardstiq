import json

from typing import Dict, Any, Optional, Tuple
from ..interfaces import (
    QPU,
    Benchmark,
    Dataset,
    QpuProvider,
    DatasetProvider,
    BenchmarkProvider,
)

from ..plugins import PROVIDER_REGISTRY


def _parse_full_name(full_name: str) -> Tuple[str, str]:
    if "/" not in full_name:
        raise ValueError(
            f"Invalid name format: '{full_name}'. Expected 'provider/resource'."
        )
    provider_name, resource_name = full_name.split("/", 1)
    return provider_name, resource_name


def _get_qpu_instance(full_qpu_name: str, config: Dict) -> QPU:
    provider_name, qpu_name = _parse_full_name(full_qpu_name)

    provider_instance = PROVIDER_REGISTRY.get(provider_name)
    if not provider_instance:
        raise KeyError(f"QPU provider not found: '{provider_name}'")
    if not isinstance(provider_instance, QpuProvider):
        raise TypeError(f"Provider '{provider_name}' is not a QpuProvider.")

    return provider_instance.get_qpu(qpu_name, config)


def _get_dataset_instance(full_dataset_name: str, config: Dict) -> Dataset:
    provider_name, dataset_name = _parse_full_name(full_dataset_name)
    provider_instance = PROVIDER_REGISTRY.get(provider_name)

    if not provider_instance:
        raise KeyError(f"Dataset provider not found: '{provider_name}'")
    if not isinstance(provider_instance, DatasetProvider):
        raise TypeError(f"Provider '{provider_name}' is not a DatasetProvider.")

    return provider_instance.get_dataset(dataset_name, config)


def _get_benchmark_instance(full_benchmark_name: str, config: Dict) -> Benchmark:
    provider_name, benchmark_name = _parse_full_name(full_benchmark_name)
    provider_instance = PROVIDER_REGISTRY.get(provider_name)

    if not provider_instance:
        raise KeyError(f"Benchmark provider not found: '{provider_name}'")
    if not isinstance(provider_instance, BenchmarkProvider):
        raise TypeError(f"Provider '{provider_name}' is not a BenchmarkProvider.")

    return provider_instance.get_benchmark(benchmark_name, config)


def run_benchmark(
    benchmark_name: str, qpu_name: str, dataset_name: Optional[str], params_json: str
) -> Dict[str, Any]:
    """
    Core implementation for running a benchmark.
    This function resolves components dynamically using providers.
    """

    try:
        config = json.loads(params_json)
    except json.JSONDecodeError:
        raise ValueError(f"Invalid JSON parameters: {params_json}")

    benchmark = _get_benchmark_instance(benchmark_name, config)
    qpu = _get_qpu_instance(qpu_name, config)

    dataset_obj = None

    if dataset_name:
        dataset = _get_dataset_instance(dataset_name, config)
        dataset_obj = dataset.load()

    circuit = benchmark.build_circuit(dataset_obj)
    results = qpu.execute(circuit=circuit, shots=config.get("shots", 1024))
    score = benchmark.score(results)

    return score
