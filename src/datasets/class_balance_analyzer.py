"""
class_balance_analyzer.py

Measures dataset balance.

Perfect balance:
1.0

Extremely imbalanced:
close to 0
"""

class ClassBalanceAnalyzer:

    def calculate(self, y):

        counts = y.value_counts()

        minority = counts.min()

        majority = counts.max()

        ratio = minority / majority

        return {
            "class_balance_ratio":
                round(float(ratio), 4)
        }