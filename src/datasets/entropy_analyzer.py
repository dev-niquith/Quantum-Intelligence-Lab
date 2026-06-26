"""
entropy_analyzer.py

Measures target entropy.

Higher entropy generally means
harder classification problems.
"""

import numpy as np


class EntropyAnalyzer:

    def calculate(self, y):

        probabilities = (
            y.value_counts(normalize=True)
            .values
        )

        entropy = -np.sum(
            probabilities *
            np.log2(probabilities)
        )

        return {
            "target_entropy":
                round(float(entropy), 4)
        }