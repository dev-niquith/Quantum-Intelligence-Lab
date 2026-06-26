"""
Dataset Intelligence Engine

Central coordinator for all
dataset analytics.
"""

from datasets.dataset_profiler import DatasetProfiler
from datasets.complexity_analyzer import ComplexityAnalyzer
from datasets.qml_suitability import QMLSuitabilityAnalyzer

from datasets.entropy_analyzer import EntropyAnalyzer
from datasets.class_balance_analyzer import (
    ClassBalanceAnalyzer
)
from datasets.correlation_analyzer import (
    CorrelationAnalyzer
)
from datasets.qri_calculator import QRICalculator


class DatasetIntelligenceEngine:

    def analyze(self, X, y):

        report = {}

        profiler = DatasetProfiler()
        complexity = ComplexityAnalyzer()
        qml = QMLSuitabilityAnalyzer()

        entropy = EntropyAnalyzer()
        balance = ClassBalanceAnalyzer()
        correlation = CorrelationAnalyzer()

        profile_data = profiler.profile(X, y)

        complexity_data = (
            complexity.calculate_complexity_score(X)
        )

        qml_data = qml.calculate(X, y)

        entropy_data = entropy.calculate(y)

        balance_data = balance.calculate(y)

        correlation_data = (
            correlation.calculate(X)
        )

        qri = QRICalculator()

        qri_data = qri.calculate(
            features=X.shape[1],
            entropy=entropy_data[
                "target_entropy"
            ],
            balance_ratio=balance_data[
                "class_balance_ratio"
            ]
        )

        report.update(profile_data)
        report.update(complexity_data)
        report.update(qml_data)
        report.update(entropy_data)
        report.update(balance_data)
        report.update(correlation_data)
        report.update(qri_data)

        return report