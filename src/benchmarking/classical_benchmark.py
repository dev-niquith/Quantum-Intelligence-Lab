"""
classical_benchmark.py

Runs classical models
through QIL evaluation engine.
"""

from models.classical.random_forest_model import (
    RandomForestModel
)

from evaluation.train_test_manager import (
    TrainTestManager
)

from evaluation.metrics_calculator import (
    MetricsCalculator
)

from evaluation.cross_validator import (
    CrossValidator
)


class ClassicalBenchmark:

    def run(
        self,
        X,
        y,
        seed
    ):

        model = (
            RandomForestModel()
            .build()
        )

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

        model.fit(
            X_train,
            y_train
        )

        predictions = (
            model.predict(X_test)
        )

        metrics = (
            MetricsCalculator()
            .calculate(
                y_test,
                predictions
            )
        )

        cv_results = (
            CrossValidator()
            .evaluate(
                model,
                X,
                y,
                folds=5
            )
        )

        metrics.update(
            cv_results
        )

        return metrics