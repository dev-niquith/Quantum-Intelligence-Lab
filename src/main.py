from src.datasets.dataset_loader import (
    DatasetLoader
)

from src.benchmarking.classical_benchmark import (
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

    results = sorted(

        results,

        key=lambda x:
        x["accuracy"],

        reverse=True
    )

    print(
        "\nCLASSICAL MODEL RANKINGS\n"
    )

    for rank, result in enumerate(
        results,
        start=1
    ):

        print(
            f"{rank}. "
            f"{result['model']}"
        )

        print(
            f"Accuracy: "
            f"{result['accuracy']}"
        )

        print(
            f"F1: "
            f"{result['f1']}"
        )

        print("-" * 30)


if __name__ == "__main__":
    main()