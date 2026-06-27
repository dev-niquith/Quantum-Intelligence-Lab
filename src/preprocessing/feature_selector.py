"""
feature_selector.py

Feature selection methods.

Used for:

- Dimensionality reduction
- Noise removal
- Quantum feature compression
"""

from sklearn.feature_selection import (
    SelectKBest,
    f_classif
)


class FeatureSelector:

    def __init__(self, k=10):

        self.selector = SelectKBest(
            score_func=f_classif,
            k=k
        )

    def fit_transform(
        self,
        X,
        y
    ):

        return self.selector.fit_transform(
            X,
            y
        )

    def transform(self, X):

        return self.selector.transform(X)