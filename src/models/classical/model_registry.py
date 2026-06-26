"""
model_registry.py

Central registry for all
classical models.
"""

from models.classical.random_forest_model import (
    RandomForestModel
)

from models.classical.logistic_regression_model import (
    LogisticRegressionModel
)

from models.classical.svm_model import (
    SVMModel
)

from models.classical.mlp_model import (
    MLPModel
)


class ModelRegistry:

    def get_models(self):

        return {

            "Random Forest":
                RandomForestModel().build(),

            "Logistic Regression":
                LogisticRegressionModel().build(),

            "SVM":
                SVMModel().build(),

            "MLP":
                MLPModel().build()
        }