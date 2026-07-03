"""
svm_model.py

Quantum Intelligence Lab (QIL)

Support Vector Machine (SVM) model implementation.
"""

from sklearn.svm import SVC

from src.core.base_model import BaseModel


class SVMModel(BaseModel):
    """
    Support Vector Machine (SVM) model.
    """

    def __init__(self):
        super().__init__(
            model_name="Support Vector Machine"
        )

    @property
    def category(self) -> str:
        """
        Model category.
        """
        return "Classical"

    def build(self) -> SVC:
        """
        Build and return the model.
        """
        return SVC(
            kernel="rbf",
            # probability=True,
            random_state=42
        )