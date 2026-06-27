"""
model_registry.py

Central registry for all
classical models.
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

    def get_models(self):

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