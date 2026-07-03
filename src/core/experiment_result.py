"""
experiment_result.py

Quantum Intelligence Lab (QIL)

Represents a complete research experiment.

An ExperimentResult contains:

• Experiment metadata
• Dataset information
• Configuration
• Benchmark results
• Optional notes

This becomes the primary object exchanged between
major subsystems such as Benchmarking, Reporting,
Database, Recommendation Engine and the AI Research
Copilot.
"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Dict, Optional

from src.core.benchmark_result import BenchmarkResult


@dataclass
class ExperimentResult:
    """
    Represents one complete research experiment.
    """

    experiment_name: str

    dataset_name: str

    benchmark_results: List[BenchmarkResult]

    timestamp: str = field(
        default_factory=lambda: datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )
    )

    configuration: Dict = field(default_factory=dict)

    researcher: str = "Unknown"

    notes: Optional[str] = None

    version: str = "0.6.0"

    # -----------------------------------------------------
    # Experiment Statistics
    # -----------------------------------------------------

    @property
    def total_models(self) -> int:
        """
        Number of benchmarked models.
        """

        return len(self.benchmark_results)

    @property
    def best_model(self) -> BenchmarkResult:
        """
        Returns the model with the highest accuracy.
        """

        return max(
            self.benchmark_results,
            key=lambda result: result.metrics.accuracy
        )

    @property
    def average_accuracy(self) -> float:
        """
        Average accuracy across all benchmarked models.
        """

        if not self.benchmark_results:
            return 0.0

        return sum(
            result.metrics.accuracy
            for result in self.benchmark_results
        ) / len(self.benchmark_results)

    # -----------------------------------------------------
    # Utility Methods
    # -----------------------------------------------------

    def summary(self) -> dict:
        """
        Returns a compact experiment summary.
        """

        best = self.best_model

        return {

            "experiment": self.experiment_name,

            "dataset": self.dataset_name,

            "timestamp": self.timestamp,

            "models_tested": self.total_models,

            "best_model": best.model_name,

            "best_accuracy": round(
                best.metrics.accuracy,
                4
            ),

            "average_accuracy": round(
                self.average_accuracy,
                4
            )
        }

    def to_dict(self) -> dict:
        """
        Convert the experiment into a serializable dictionary.

        Useful for exporting to JSON or databases.
        """

        return {

            "experiment_name": self.experiment_name,

            "dataset_name": self.dataset_name,

            "timestamp": self.timestamp,

            "researcher": self.researcher,

            "version": self.version,

            "configuration": self.configuration,

            "notes": self.notes,

            "benchmark_results": [

                result.to_dict()

                for result in self.benchmark_results

            ]
        }

    def __repr__(self):

        return (

            "ExperimentResult("

            f"experiment='{self.experiment_name}', "

            f"dataset='{self.dataset_name}', "

            f"models={self.total_models})"

        )