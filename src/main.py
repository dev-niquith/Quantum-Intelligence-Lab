from datasets.dataset_loader import (
    DatasetLoader
)

from benchmarking.classical_benchmark import (
    ClassicalBenchmark
)


def main():

    print("\n")
    print("=" * 60)
    print("QUANTUM INTELLIGENCE LAB")
    print("=" * 60)

    loader = DatasetLoader()

    X, y = loader.load_dataset(
        "breast_cancer"
    )

    benchmark = (
        ClassicalBenchmark()
    )

    results = benchmark.run(
        X,
        y,
        seed=42
    )

    print(
        "\nBenchmark Results\n"
    )

    for key, value in results.items():

        print(
            f"{key}: {value}"
        )


if __name__ == "__main__":
    main()