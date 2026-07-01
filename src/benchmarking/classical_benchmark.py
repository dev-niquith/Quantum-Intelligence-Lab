"""
classical_benchmark.py

Quantum Intelligence Lab (QIL)

Research-grade Classical Benchmark Engine.

This module benchmarks multiple classical machine learning models
using the Cross Validation Engine.

Unlike simple benchmark scripts, this implementation:

✓ Uses research-grade cross validation
✓ Computes statistical summaries
✓ Produces reproducible evaluations
✓ Is model-agnostic
✓ Can later benchmark Quantum and Hybrid models
without architectural changes.
"""

from typing import List

import pandas as pd

from src.evaluation.cross_validator import CrossValidator


class ClassicalBenchmark:
    """
    Research Benchmark Engine.

    This class evaluates every model supplied by the
    Model Registry and returns a ranked leaderboard.
    """

    def __init__(
        self,
        folds: int = 5,
        random_seed: int = 42
    ):

        self.cross_validator = CrossValidator(
            folds=folds,
            random_seed=random_seed
        )

    def evaluate_models(
        self,
        models: List,
        X,
        y
    ) -> pd.DataFrame:
        """
        Evaluate every supplied model.

        Parameters
        ----------
        models

            List of tuples

            Example

            [
                ("Random Forest", rf_model),
                ("SVM", svm_model)
            ]

        Returns
        -------
        pandas DataFrame

            Ranked leaderboard.
        """

        leaderboard = []

        for model_name, model in models:

            print(f"\nEvaluating {model_name}...")

            statistics = self.cross_validator.evaluate(
                model,
                X,
                y
            )

            leaderboard.append(

                {

                    "model": model_name,

                    "accuracy": statistics["accuracy"]["mean"],

                    "precision": statistics["precision"]["mean"],

                    "recall": statistics["recall"]["mean"],

                    "f1": statistics["f1"]["mean"],

                    "accuracy_std":
                        statistics["accuracy"]["standard_deviation"],

                    "precision_std":
                        statistics["precision"]["standard_deviation"],

                    "recall_std":
                        statistics["recall"]["standard_deviation"],

                    "f1_std":
                        statistics["f1"]["standard_deviation"],

                    "accuracy_ci_lower":
                        statistics["accuracy"]["confidence_interval_lower"],

                    "accuracy_ci_upper":
                        statistics["accuracy"]["confidence_interval_upper"],

                    "full_statistics": statistics

                }

            )

        leaderboard = pd.DataFrame(
            leaderboard
        )

        leaderboard = leaderboard.sort_values(
            by="accuracy",
            ascending=False
        )

        leaderboard.reset_index(
            drop=True,
            inplace=True
        )

        leaderboard.insert(
            0,
            "rank",
            range(
                1,
                len(leaderboard) + 1
            )
        )

        return leaderboard

    def print_results(
        self,
        leaderboard: pd.DataFrame
    ):
        """
        Print benchmark results.
        """

        print()

        print("=" * 60)
        print("CLASSICAL RESEARCH BENCHMARK")
        print("=" * 60)

        for _, row in leaderboard.iterrows():

            print()

            print(f"Rank : {row['rank']}")
            print(f"Model : {row['model']}")

            print(
                f"Mean Accuracy : {row['accuracy']:.4f}"
            )

            print(
                f"Std Dev       : {row['accuracy_std']:.4f}"
            )

            print(

                "95% CI        : "

                f"[{row['accuracy_ci_lower']:.4f}, "

                f"{row['accuracy_ci_upper']:.4f}]"

            )

            print("-" * 40)