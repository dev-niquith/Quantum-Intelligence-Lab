"""
logistic_regression_model.py

Quantum Intelligence Lab (QIL)

Logistic Regression model implementation.
"""

from sklearn.linear_model import LogisticRegression

from src.core.base_model import BaseModel


class LogisticRegressionModel(BaseModel):
    """
    Logistic Regression model.
    """

    def __init__(self):

        super().__init__(
            model_name="Logistic Regression"
        )

    @property
    def category(self):
        """
        Model category.
        """

        return "Classical"

    def build(self):
        """
        Build and return the model.
        """

        return LogisticRegression(
            max_iter=1000,
            random_state=42
        )