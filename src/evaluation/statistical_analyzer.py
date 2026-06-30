"""
statistical_analyzer.py

Quantum Intelligence Lab (QIL)

This module provides statistical analysis utilities for
research-grade model evaluation.

Purpose
-------
Instead of evaluating a model from a single train/test split,
research typically evaluates performance across multiple folds
using Cross Validation.

Example:

Accuracy Scores

Fold 1 : 0.962
Fold 2 : 0.955
Fold 3 : 0.968
Fold 4 : 0.951
Fold 5 : 0.964

↓

Mean Accuracy
Standard Deviation
Minimum
Maximum
95% Confidence Interval

This class is completely model-independent.

It works for:

- Classical ML
- Quantum ML
- Hybrid Quantum-Classical ML

Future modules such as:

- Stability Analysis
- Recommendation Engine
- AI Research Copilot

will consume the outputs of this class.
"""

from typing import Dict, List

import numpy as np


class StatisticalAnalyzer:
    """
    Computes descriptive statistics for
    cross-validation experiments.
    """

    def analyze(
        self,
        values: List[float]
    ) -> Dict[str, float]:
        """
        Compute statistical summary.

        Parameters
        ----------
        values : List[float]

            Metric values collected across folds.

        Returns
        -------
        Dict[str, float]

            Research statistics.
        """

        if len(values) == 0:
            raise ValueError(
                "Statistics cannot be computed on an empty list."
            )

        values = np.asarray(values)

        mean = np.mean(values)

        std = np.std(
            values,
            ddof=1
        ) if len(values) > 1 else 0.0

        minimum = np.min(values)

        maximum = np.max(values)

        median = np.median(values)

        # ----------------------------------------
        # 95% Confidence Interval
        # ----------------------------------------

        if len(values) > 1:

            margin = (
                1.96
                * std
                / np.sqrt(len(values))
            )

        else:

            margin = 0.0

        return {

            "mean": round(
                float(mean),
                4
            ),

            "median": round(
                float(median),
                4
            ),

            "minimum": round(
                float(minimum),
                4
            ),

            "maximum": round(
                float(maximum),
                4
            ),

            "standard_deviation": round(
                float(std),
                4
            ),

            "confidence_interval_lower": round(
                float(mean - margin),
                4
            ),

            "confidence_interval_upper": round(
                float(mean + margin),
                4
            )

        }

    def print_summary(
        self,
        statistics: Dict[str, float]
    ) -> None:
        """
        Pretty-print statistics.

        This function is useful while
        developing and debugging.
        """

        print()

        print("=" * 60)
        print("STATISTICAL ANALYSIS")
        print("=" * 60)

        print(
            f"Mean                 : {statistics['mean']}"
        )

        print(
            f"Median               : {statistics['median']}"
        )

        print(
            f"Minimum              : {statistics['minimum']}"
        )

        print(
            f"Maximum              : {statistics['maximum']}"
        )

        print(
            f"Standard Deviation   : {statistics['standard_deviation']}"
        )

        print(
            "95% Confidence Interval"
        )

        print(
            f"Lower Bound          : {statistics['confidence_interval_lower']}"
        )

        print(
            f"Upper Bound          : {statistics['confidence_interval_upper']}"
        )