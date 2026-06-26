"""
metrics_calculator.py

Centralized metric computation.

Every model in QIL will use
this class for evaluation.
"""

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score
)


class MetricsCalculator:

    def calculate(
        self,
        y_true,
        y_pred
    ):

        return {

            "accuracy":
                round(
                    accuracy_score(
                        y_true,
                        y_pred
                    ),
                    4
                ),

            "precision":
                round(
                    precision_score(
                        y_true,
                        y_pred,
                        average="weighted"
                    ),
                    4
                ),

            "recall":
                round(
                    recall_score(
                        y_true,
                        y_pred,
                        average="weighted"
                    ),
                    4
                ),

            "f1":
                round(
                    f1_score(
                        y_true,
                        y_pred,
                        average="weighted"
                    ),
                    4
                )
        }