"""
logistic_regression_model.py

Logistic Regression model.
"""

from sklearn.linear_model import (
    LogisticRegression
)


class LogisticRegressionModel:

    def build(self):

        return LogisticRegression(

            max_iter=500,

            random_state=42
        )