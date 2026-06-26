"""
complexity_analyzer.py

Purpose:
--------
Estimate how difficult
a dataset is.

This is NOT a formal
research metric.

Instead it provides
a practical heuristic.
"""

import numpy as np


class ComplexityAnalyzer:

    def calculate_complexity_score(self, X):

        samples = len(X)
        features = X.shape[1]

        feature_to_sample_ratio = features / samples

        score = min(
            100,
            int(feature_to_sample_ratio * 1000)
        )

        return {
            "feature_sample_ratio":
                round(feature_to_sample_ratio, 4),

            "complexity_score":
                score
        }