"""
model_registry.py

Quantum Intelligence Lab (QIL)

Central registry for all classical machine learning models.

The registry provides a standardized interface for retrieving
all available models. Future benchmark engines (Classical,
Quantum, and Hybrid) will consume registries instead of
instantiating models directly.

This keeps benchmarking code completely independent of the
actual model implementations.
"""

from src.models.classical.random_forest_model import RandomForestModel
from src.models.classical.logistic_regression_model import LogisticRegressionModel
from src.models.classical.svm_model import SVMModel
from src.models.classical.mlp_model import MLPModel
from src.models.classical.xgboost_model import XGBoostModel


class ModelRegistry:
    """
    Registry containing all available classical models.
    """

    def __init__(self):

        self._models = [

            (
                "Random Forest",
                RandomForestModel().build()
            ),

            (
                "Logistic Regression",
                LogisticRegressionModel().build()
            ),

            (
                "SVM",
                SVMModel().build()
            ),

            (
                "MLP",
                MLPModel().build()
            ),

            (
                "XGBoost",
                XGBoostModel().build()
            )

        ]

    def get_models(self):
        """
        Returns
        -------
        list

            List of tuples:

            [
                ("Random Forest", model),
                ("SVM", model)
            ]
        """

        return self._models

    def get_model_names(self):
        """
        Returns
        -------
        list[str]

            Names of registered models.
        """

        return [

            name

            for name, _ in self._models

        ]

    def count(self):
        """
        Returns the number of registered models.
        """

        return len(self._models)