import json

from typing import Dict, Any, Optional, Tuple
from ..interfaces import (
    Backend,
    Benchmark,
    Dataset,
    BackendProvider,
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


def _get_backend_instance(full_backend_name: str) -> Backend:
    provider_name, backend_name = _parse_full_name(full_backend_name)
    provider_instance = PROVIDER_REGISTRY.get(provider_name)

    if not provider_instance:
        raise KeyError(f"Backend provider not found: '{provider_name}'")
    if not isinstance(provider_instance, BackendProvider):
        raise TypeError(f"Provider '{provider_name}' is not a BackendProvider.")

    return provider_instance.get_backend(backend_name)


def _get_dataset_instance(full_dataset_name: str) -> Dataset:
    provider_name, dataset_name = _parse_full_name(full_dataset_name)
    provider_instance = PROVIDER_REGISTRY.get(provider_name)

    if not provider_instance:
        raise KeyError(f"Dataset provider not found: '{provider_name}'")
    if not isinstance(provider_instance, DatasetProvider):
        raise TypeError(f"Provider '{provider_name}' is not a DatasetProvider.")

    return provider_instance.get_dataset(dataset_name)


def _get_benchmark_instance(full_benchmark_name: str) -> Benchmark:
    provider_name, benchmark_name = _parse_full_name(full_benchmark_name)
    provider_instance = PROVIDER_REGISTRY.get(provider_name)

    if not provider_instance:
        raise KeyError(f"Benchmark provider not found: '{provider_name}'")
    if not isinstance(provider_instance, BenchmarkProvider):
        raise TypeError(f"Provider '{provider_name}' is not a BenchmarkProvider.")

    return provider_instance.get_benchmark(benchmark_name)


def run_benchmark(
    benchmark_name: str,
    backend_name: str,
    dataset_name: Optional[str],
    params_json: str,
) -> Dict[str, Any]:
    """
    Core implementation for running a benchmark.
    This function resolves components dynamically using providers.
    """

    try:
        config = json.loads(params_json)
    except json.JSONDecodeError:
        raise ValueError(f"Invalid JSON parameters: {params_json}")

    benchmark = _get_benchmark_instance(benchmark_name)
    backend = _get_backend_instance(backend_name)

    if dataset_name:
        dataset = _get_dataset_instance(dataset_name)
        dataset.load()

    model = benchmark.build_model(dataset=dataset)
    results = backend.run(model=model, shots=config.get("shots", 1024))
    score = benchmark.score(results)

    return score
