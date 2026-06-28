"""
main.py

QIL Main Application
"""

from src.datasets.dataset_loader import (
    DatasetLoader
)

from src.benchmarking.classical_benchmark import (
    ClassicalBenchmark
)

from src.reporting.comparison_matrix import (
    ComparisonMatrix
)


def main():

    print("\n")
    print("=" * 60)
    print("QUANTUM INTELLIGENCE LAB")
    print("=" * 60)

    # --------------------------------
    # Load Dataset
    # --------------------------------

    loader = DatasetLoader()

    X, y = loader.load_dataset(
        "breast_cancer"
    )

    # --------------------------------
    # Run Benchmark
    # --------------------------------

    benchmark = (
        ClassicalBenchmark()
    )

    results = benchmark.run(
        X,
        y,
        seed=42
    )

    # --------------------------------
    # Comparison Matrix
    # --------------------------------

    matrix = (
        ComparisonMatrix()
    )

    df = matrix.generate(
        results
    )

    matrix.display(df)

    matrix.save_csv(
        df,
        "reports/benchmark_results.csv"
    )

    print(
        "\nReport Saved:"
    )

    print(
        "reports/benchmark_results.csv"
    )


if __name__ == "__main__":
    main()