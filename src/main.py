"""
main.py

Quantum Intelligence Lab (QIL)

Main application entry point.
"""

from src.datasets.dataset_loader import DatasetLoader

from src.models.classical.model_registry import ModelRegistry

from src.benchmarking.classical_benchmark import ClassicalBenchmark

from src.reporting.comparison_matrix import ComparisonMatrix


def main():

    print()
    print("=" * 60)
    print("QUANTUM INTELLIGENCE LAB")
    print("=" * 60)

    # -------------------------------------------------
    # Load Dataset
    # -------------------------------------------------

    loader = DatasetLoader()

    X, y = loader.load_dataset(
        "breast_cancer"
    )

    # -------------------------------------------------
    # Load Models
    # -------------------------------------------------

    registry = ModelRegistry()

    models = registry.get_models()

    # -------------------------------------------------
    # Run Benchmark
    # -------------------------------------------------

    benchmark = ClassicalBenchmark(
        folds=5,
        random_seed=42
    )

    leaderboard = benchmark.evaluate_models(
        models=models,
        X=X,
        y=y
    )

    benchmark.print_results(
        leaderboard
    )

    # -------------------------------------------------
    # Generate Comparison Matrix
    # -------------------------------------------------

    comparison = ComparisonMatrix()

    comparison.generate(
        leaderboard
    )


if __name__ == "__main__":
    main()