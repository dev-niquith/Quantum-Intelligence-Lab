"""
mlp_model.py

Quantum Intelligence Lab (QIL)

Multi-Layer Perceptron (MLP) model implementation.
"""

from sklearn.neural_network import MLPClassifier

from src.core.base_model import BaseModel


class MLPModel(BaseModel):
    """
    Multi-Layer Perceptron model.
    """

    def __init__(self):

        super().__init__(
            model_name="MLP"
        )

    @property
    def category(self):
        """
        Model category.
        """

        return "Classical"

    def build(self):
        """
        Build and return the MLP classifier.
        """

        return MLPClassifier(
            hidden_layer_sizes=(64, 32),
            max_iter=1000,
            random_state=42
        )