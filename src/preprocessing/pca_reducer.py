"""
pca_reducer.py

Principal Component Analysis.

Future use:

30 features
↓
8 features
↓
QSVM
"""

from sklearn.decomposition import PCA


class PCAReducer:

    def __init__(
        self,
        n_components=8
    ):

        self.pca = PCA(
            n_components=n_components
        )

    def fit_transform(self, X):

        return self.pca.fit_transform(X)

    def transform(self, X):

        return self.pca.transform(X)

    def explained_variance(self):

        return self.pca.explained_variance_ratio_