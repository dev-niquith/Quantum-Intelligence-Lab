"""
random_forest_model.py

Quantum Intelligence Lab (QIL)

Random Forest model implementation.
"""

from sklearn.ensemble import RandomForestClassifier

from src.core.base_model import BaseModel


class RandomForestModel(BaseModel):
    """
    Random Forest model.
    """

    def __init__(self):
        super().__init__(
            model_name="Random Forest"
        )

    @property
    def category(self) -> str:
        """
        Model category.
        """
        return "Classical"

    def build(self) -> RandomForestClassifier:
        """
        Build and return the model.
        """
        return RandomForestClassifier(
            n_estimators=100,
            random_state=42
        )