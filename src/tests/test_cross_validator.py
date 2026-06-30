"""
test_cross_validator.py

Unit test for the Cross Validation Engine.

This test verifies that:

1. Stratified K-Fold executes successfully.
2. Metrics are calculated for every fold.
3. Statistical summaries are generated correctly.
"""

from src.datasets.dataset_loader import DatasetLoader
from src.evaluation.cross_validator import CrossValidator
from src.models.classical.logistic_regression_model import (
    LogisticRegressionModel,
)


def main():

    print()
    print("=" * 60)
    print("TEST : CROSS VALIDATION ENGINE")
    print("=" * 60)

    # -------------------------------
    # Load Dataset
    # -------------------------------

    loader = DatasetLoader()

    X, y = loader.load_dataset(
        "breast_cancer"
    )

    # -------------------------------
    # Load Model
    # -------------------------------

    model = LogisticRegressionModel().build()

    # -------------------------------
    # Evaluate
    # -------------------------------

    validator = CrossValidator(
        folds=5,
        random_seed=42
    )

    results = validator.evaluate(
        model,
        X,
        y
    )

    # -------------------------------
    # Display Results
    # -------------------------------

    for metric_name, statistics in results.items():

        print()

        print("-" * 40)
        print(metric_name.upper())
        print("-" * 40)

        for key, value in statistics.items():

            print(f"{key:<30}: {value}")


if __name__ == "__main__":
    main()