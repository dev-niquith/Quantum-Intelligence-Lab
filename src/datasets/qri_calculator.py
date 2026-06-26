"""
qri_calculator.py

QRI

Quantum Readiness Index

0 - 100
"""

class QRICalculator:

    def calculate(
        self,
        features,
        entropy,
        balance_ratio
    ):

        score = 0

        if features > 20:
            score += 40

        elif features > 10:
            score += 20

        if entropy > 0.9:
            score += 30

        elif entropy > 0.5:
            score += 15

        if balance_ratio > 0.5:
            score += 30

        return {
            "qri_score":
                min(score, 100)
        }