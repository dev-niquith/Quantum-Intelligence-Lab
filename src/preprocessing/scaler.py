"""
scaler.py

Feature scaling module.

Standardization is required for:

- Logistic Regression
- SVM
- MLP
- QSVM
- VQC
"""

from sklearn.preprocessing import StandardScaler


class DataScaler:

    def __init__(self):

        self.scaler = StandardScaler()

    def fit_transform(self, X):

        return self.scaler.fit_transform(X)

    def transform(self, X):

        return self.scaler.transform(X)