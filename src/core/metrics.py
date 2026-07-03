"""
metrics.py

Quantum Intelligence Lab (QIL)

Defines the Metrics domain object.

Every benchmark returns one Metrics object,
making metric handling consistent throughout
the platform.
"""

from dataclasses import dataclass


@dataclass
class Metrics:
    """
    Standard metrics produced by benchmarking.

    Attributes
    ----------
    accuracy : float
        Mean accuracy.

    precision : float
        Mean precision.

    recall : float
        Mean recall.

    f1 : float
        Mean F1-score.

    accuracy_std : float
        Standard deviation of accuracy.

    confidence_lower : float
        Lower bound of the confidence interval.

    confidence_upper : float
        Upper bound of the confidence interval.
    """

    accuracy: float

    precision: float

    recall: float

    f1: float

    accuracy_std: float

    confidence_lower: float

    confidence_upper: float

    def to_dict(self):
        """
        Convert metrics into a dictionary.

        Returns
        -------
        dict
        """

        return {

            "accuracy": self.accuracy,

            "precision": self.precision,

            "recall": self.recall,

            "f1": self.f1,

            "accuracy_std": self.accuracy_std,

            "confidence_lower": self.confidence_lower,

            "confidence_upper": self.confidence_upper

        }

    def __repr__(self):

        return (

            "Metrics("

            f"accuracy={self.accuracy:.4f}, "

            f"f1={self.f1:.4f})"

        )