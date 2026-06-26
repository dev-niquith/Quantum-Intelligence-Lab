"""
cross_validator.py

Handles k-fold cross validation.
"""

from sklearn.model_selection import (
    cross_val_score
)

import numpy as np


class CrossValidator:

    def evaluate(
        self,
        model,
        X,
        y,
        folds=5
    ):

        scores = cross_val_score(
            model,
            X,
            y,
            cv=folds,
            scoring="accuracy"
        )

        return {

            "cv_mean_accuracy":
                round(
                    float(
                        np.mean(scores)
                    ),
                    4
                ),

            "cv_std":
                round(
                    float(
                        np.std(scores)
                    ),
                    4
                )
        }