"""
random_forest_model.py

First baseline model.

Used to validate
evaluation framework.
"""

from sklearn.ensemble import (
    RandomForestClassifier
)


class RandomForestModel:

    def build(self):

        return RandomForestClassifier(

            n_estimators=100,

            random_state=42
        )