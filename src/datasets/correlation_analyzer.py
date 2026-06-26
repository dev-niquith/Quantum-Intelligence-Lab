"""
correlation_analyzer.py

Measures average feature correlation.

High correlation may indicate
feature redundancy.
"""

import numpy as np


class CorrelationAnalyzer:

    def calculate(self, X):

        corr_matrix = X.corr().abs()

        upper = corr_matrix.where(
            np.triu(
                np.ones(corr_matrix.shape),
                k=1
            ).astype(bool)
        )

        avg_corr = upper.stack().mean()

        return {
            "average_feature_correlation":
                round(float(avg_corr), 4)
        }