"""
benchmark_result.py

Quantum Intelligence Lab (QIL)

Represents the benchmarking result of a
single machine learning model.
"""

from dataclasses import dataclass
from typing import Optional

from src.core.metrics import Metrics


@dataclass
class BenchmarkResult:
    """
    Stores the outcome of benchmarking one model.

    Attributes
    ----------
    model_name : str
        Name of the model.

    category : str
        Classical / Quantum / Hybrid.

    metrics : Metrics
        Performance statistics.

    training_time : float
        Time required for training.

    inference_time : float
        Time required for prediction.

    notes : str
        Optional notes.
    """

    model_name: str

    category: str

    metrics: Metrics

    training_time: float = 0.0

    inference_time: float = 0.0

    notes: Optional[str] = None

    def to_dict(self):
        """
        Convert BenchmarkResult into a dictionary.

        Useful when exporting to CSV,
        DataFrames or databases.
        """

        data = {

            "model": self.model_name,

            "category": self.category,

            "training_time": self.training_time,

            "inference_time": self.inference_time

        }

        data.update(self.metrics.to_dict())

        data["notes"] = self.notes

        return data

    def summary(self):
        """
        Return a compact summary for console output.
        """

        return {

            "model": self.model_name,

            "accuracy": round(
                self.metrics.accuracy,
                4
            ),

            "f1": round(
                self.metrics.f1,
                4
            )

        }

    def __repr__(self):

        return (

            "BenchmarkResult("

            f"model='{self.model_name}', "

            f"category='{self.category}', "

            f"accuracy={self.metrics.accuracy:.4f})"

        )