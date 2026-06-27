"""
classical_benchmark.py

Runs all classical models through:

Dataset
    ↓
Train/Test Split
    ↓
Preprocessing
    ↓
Model
    ↓
Evaluation
"""

from src.evaluation.metrics_calculator import (
    MetricsCalculator
)

from src.evaluation.train_test_manager import (
    TrainTestManager
)

from src.models.classical.model_registry import (
    ModelRegistry
)

from src.preprocessing.preprocessing_pipeline import (
    PreprocessingPipeline
)


class ClassicalBenchmark:

    def run(
        self,
        X,
        y,
        seed
    ):

        splitter = TrainTestManager()

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

        registry = ModelRegistry()

        results = []

        for (
            model_name,
            model
        ) in registry.get_models().items():

            # --------------------------
            # PREPROCESSING
            # --------------------------

            pipeline = (
                PreprocessingPipeline(
                    k_features=15,
                    pca_components=8
                )
            )

            X_train_processed = (
                pipeline.fit_transform(
                    X_train,
                    y_train
                )
            )

            X_test_processed = (
                pipeline.transform(
                    X_test
                )
            )

            # --------------------------
            # TRAIN
            # --------------------------

            model.fit(
                X_train_processed,
                y_train
            )

            predictions = (
                model.predict(
                    X_test_processed
                )
            )

            # --------------------------
            # EVALUATE
            # --------------------------

            metrics = (
                MetricsCalculator()
                .calculate(
                    y_test,
                    predictions
                )
            )

            results.append({

                "model": model_name,

                **metrics
            })

        return results