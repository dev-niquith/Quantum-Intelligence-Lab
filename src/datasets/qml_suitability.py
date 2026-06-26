"""
qml_suitability.py

Purpose:
--------
Estimate whether a dataset
might benefit from QML.

IMPORTANT:
-----------
This is a heuristic score.

It is NOT scientific proof.
"""


class QMLSuitabilityAnalyzer:

    def calculate(self, X, y):

        score = 0

        features = X.shape[1]
        classes = y.nunique()

        # More features
        if features > 10:
            score += 30

        # Multi-class problems
        if classes > 2:
            score += 20

        # Larger datasets
        if len(X) > 500:
            score += 20

        # Extra bonus
        if features > 20:
            score += 30

        score = min(score, 100)

        return {
            "qml_suitability_score": score
        }