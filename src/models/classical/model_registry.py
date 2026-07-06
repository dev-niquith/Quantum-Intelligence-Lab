"""
model_registry.py

Quantum Intelligence Lab (QIL)

Central registry for all
classical machine learning models.
"""

from src.models.classical.random_forest_model import (
    RandomForestModel
)

from src.models.classical.logistic_regression_model import (
    LogisticRegressionModel
)

from src.models.classical.svm_model import (
    SVMModel
)

from src.models.classical.mlp_model import (
    MLPModel
)

from src.models.classical.xgboost_model import (
    XGBoostModel
)


class ModelRegistry:
    """
    Registry responsible for managing all
    classical machine learning models.
    """

    def get_models(self):
        """
        Return all registered models.

        Returns
        -------
        dict

            Dictionary containing

            model_name -> model_object
        """

        return {

            "Random Forest":
                RandomForestModel().build(),

            "Logistic Regression":
                LogisticRegressionModel().build(),

            "SVM":
                SVMModel().build(),

            "MLP":
                MLPModel().build(),

            "XGBoost":
                XGBoostModel().build()

        }

    def available_models(self):
        """
        Return all registered model names.
        """

        return list(

            self.get_models().keys()

        )

    def total_models(self):
        """
        Return the total number of
        registered models.
        """

        return len(

            self.get_models()

        )

    def __repr__(self):

        return (

            "ModelRegistry("

            f"{self.total_models()} "

            "registered models)"

        )