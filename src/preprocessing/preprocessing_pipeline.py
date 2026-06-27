"""
preprocessing_pipeline.py

Central preprocessing engine.

Pipeline:

Scale
↓
Feature Selection
↓
PCA
"""

from src.preprocessing.scaler import (
    DataScaler
)

from src.preprocessing.feature_selector import (
    FeatureSelector
)

from src.preprocessing.pca_reducer import (
    PCAReducer
)


class PreprocessingPipeline:

    def __init__(
        self,
        k_features=15,
        pca_components=8
    ):

        self.scaler = DataScaler()

        self.selector = FeatureSelector(
            k=k_features
        )

        self.reducer = PCAReducer(
            n_components=pca_components
        )

    def fit_transform(
        self,
        X,
        y
    ):

        X = (
            self.scaler
            .fit_transform(X)
        )

        X = (
            self.selector
            .fit_transform(X, y)
        )

        X = (
            self.reducer
            .fit_transform(X)
        )

        return X

    def transform(self, X):

        X = (
            self.scaler
            .transform(X)
        )

        X = (
            self.selector
            .transform(X)
        )

        X = (
            self.reducer
            .transform(X)
        )

        return X