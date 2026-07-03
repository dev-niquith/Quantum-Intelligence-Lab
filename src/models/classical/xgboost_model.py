"""
xgboost_model.py

Quantum Intelligence Lab (QIL)

XGBoost model implementation.
"""

from xgboost import XGBClassifier

from src.core.base_model import BaseModel


class XGBoostModel(BaseModel):
    """
    XGBoost classifier.
    """

    def __init__(self):

        super().__init__(
            model_name="XGBoost"
        )

    @property
    def category(self):
        """
        Model category.
        """

        return "Classical"

    def build(self):
        """
        Build and return the XGBoost model.
        """

        return XGBClassifier(
            n_estimators=100,
            max_depth=4,
            learning_rate=0.1,
            random_state=42,
            eval_metric="logloss"
        )