"""
classical_benchmark.py

Runs all classical models.
"""

from evaluation.metrics_calculator import (
    MetricsCalculator
)

from evaluation.train_test_manager import (
    TrainTestManager
)

from models.classical.model_registry import (
    ModelRegistry
)


class ClassicalBenchmark:

    def run(
        self,
        X,
        y,
        seed
    ):

        splitter = (
            TrainTestManager()
        )

        (
            X_train,
            X_test,
            y_train,
            y_test
        ) = splitter.split(
            X,
            y,
            seed
        )

        registry = (
            ModelRegistry()
        )

        results = []

        for (
            model_name,
            model
        ) in registry.get_models().items():

            model.fit(
                X_train,
                y_train
            )

            predictions = (
                model.predict(
                    X_test
                )
            )

            metrics = (
                MetricsCalculator()
                .calculate(
                    y_test,
                    predictions
                )
            )

            results.append({

                "model":
                    model_name,

                **metrics
            })

        return results