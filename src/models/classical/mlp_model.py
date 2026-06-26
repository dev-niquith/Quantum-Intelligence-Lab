"""
mlp_model.py

Multi-Layer Perceptron.
"""

from sklearn.neural_network import (
    MLPClassifier
)


class MLPModel:

    def build(self):

        return MLPClassifier(

            hidden_layer_sizes=(64, 32),

            max_iter=500,

            random_state=42
        )