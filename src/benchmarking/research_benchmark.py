"""
research_benchmark.py

Quantum Intelligence Lab (QIL)

Unified Research Benchmark Engine

This module is responsible for benchmarking
all machine learning approaches supported
by QIL.

Supported Categories
--------------------

• Classical Machine Learning
• Quantum Machine Learning
• Hybrid Quantum-Classical Models (future)

Responsibilities
----------------

✓ Dataset preprocessing

✓ Classical benchmarking

✓ Quantum benchmarking

✓ Leaderboard generation

✓ Research statistics

✓ Report generation

✓ CSV export

✓ Future AI recommendation integration
"""

#Part 1


from __future__ import annotations

#from logging import config
import time

from typing import Dict
from typing import List

import pandas as pd

from src.evaluation.cross_validator import CrossValidator

from src.preprocessing.preprocessing_pipeline import (
    PreprocessingPipeline
)

from src.reporting.comparison_matrix import (
    ComparisonMatrix
)

from src.models.classical.model_registry import (
    ModelRegistry
)

from src.models.quantum.quantum_registry import (
    QuantumRegistry
)


class ResearchBenchmark:
    """
    Unified Benchmark Engine.

    Every model inside QIL is evaluated
    through this class.

    The benchmark engine is intentionally
    model-agnostic.

    It never needs to know whether a model is

    • Classical

    • Quantum

    • Hybrid

    As long as a registry returns a model,
    it can be benchmarked.
    """

    def __init__(
        self,
        folds: int = 5,
        random_seed: int = 42
    ):

        # ----------------------------------
        # Cross Validation Engine
        # ----------------------------------

        self.cross_validator = CrossValidator(

            folds=folds,

            random_seed=random_seed

        )

        # ----------------------------------
        # Research Preprocessing Pipeline
        # ----------------------------------

        self.preprocessing = (
            PreprocessingPipeline()
        )

        # ----------------------------------
        # Reporting
        # ----------------------------------

        self.comparison_matrix = (
            ComparisonMatrix()
        )

        # ----------------------------------
        # Registries
        # ----------------------------------

        self.classical_registry = (
            ModelRegistry()
        )

        self.quantum_registry = (
            QuantumRegistry()
        )

    # ======================================================
    # DATA PREPARATION
    # ======================================================

    def preprocess_dataset(
        self,
        X,
        y
    ):
        """
        Execute the complete research
        preprocessing pipeline.

        Returns
        -------

        Processed features and labels.
        """

        print()

        print("=" * 60)
        print("PREPROCESSING DATASET")
        print("=" * 60)

        X_processed = self.preprocessing.fit_transform(
            X,
            y
        )

        print()

        print("Original Shape : ", X.shape)
        print("Processed Shape:", X_processed.shape)

        return X_processed, y

    # ======================================================
    # INTERNAL MODEL EVALUATION
    # ======================================================

    def _evaluate_registry(
        self,
        registry,
        category: str,
        X,
        y
    ) -> List[Dict]:
        """
        Evaluate every model contained
        inside a registry.

        Parameters
        ----------

        registry

            Registry object.

        category

            Classical

            Quantum

            Hybrid

        Returns
        -------

        List of benchmark dictionaries.
        """

        leaderboard = []

        models = registry.get_models()

        print()

        print("=" * 60)
        print(f"EVALUATING {category.upper()} MODELS")
        print("=" * 60)

        for model_name, model in models.items():

            print()

            print(f"Evaluating {model_name}...")

            start_time = time.perf_counter()

            statistics = self.cross_validator.evaluate(

                model,

                X,

                y

            )

            elapsed = (
                time.perf_counter()
                - start_time
            )

            leaderboard.append(

                {

                    "category": category,

                    "model": model_name,

                    "accuracy":
                        statistics["accuracy"]["mean"],

                    "precision":
                        statistics["precision"]["mean"],

                    "recall":
                        statistics["recall"]["mean"],

                    "f1":
                        statistics["f1"]["mean"],

                    "accuracy_std":
                        statistics["accuracy"][
                            "standard_deviation"
                        ],

                    "accuracy_ci_lower":
                        statistics["accuracy"][
                            "confidence_interval_lower"
                        ],

                    "accuracy_ci_upper":
                        statistics["accuracy"][
                            "confidence_interval_upper"
                        ],

                    "training_time":
                        elapsed,

                    "statistics":
                        statistics

                }

            )

        return leaderboard
    

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
    
    #Part 2   
            
    # ======================================================    
    # CLASSICAL BENCHMARK
    # ======================================================

    def evaluate_classical(
        self,
        X,
        y
    ) -> List[Dict]:
        """
        Evaluate every registered
        classical model.
        """

        return self._evaluate_registry(

            registry=self.classical_registry,

            category="Classical",

            X=X,

            y=y

        )

    # ======================================================
    # QUANTUM BENCHMARK
    # ======================================================

    def evaluate_quantum(
        self,
        X,
        y
    ) -> List[Dict]:
        """
        Evaluate every registered
        quantum model.
        """

        return self._evaluate_registry(

            registry=self.quantum_registry,

            category="Quantum",

            X=X,

            y=y

        )

    # ======================================================
    # FUTURE HYBRID BENCHMARK
    # ======================================================

    def evaluate_hybrid(
        self,
        X,
        y
    ) -> List[Dict]:
        """
        Placeholder for Hybrid Quantum-Classical
        models.

        Hybrid benchmarking will be added in
        QIL v2.0.
        """

        return []

    # ======================================================
    # MERGE RESULTS
    # ======================================================

    def _merge_results(
        self,
        *leaderboards
    ) -> pd.DataFrame:
        """
        Merge multiple benchmark results into
        one unified research leaderboard.
        """

        merged = []

        for leaderboard in leaderboards:

            merged.extend(leaderboard)

        dataframe = pd.DataFrame(merged)

        if dataframe.empty:

            return dataframe

        dataframe = (

            dataframe

            .sort_values(

                by="accuracy",

                ascending=False

            )

            .reset_index(drop=True)

        )

        dataframe.insert(

            0,

            "rank",

            range(

                1,

                len(dataframe) + 1

            )

        )

        return dataframe

    # ======================================================
    # MAIN PIPELINE
    # ======================================================

    def run(
        self,
        X,
        y,
        preprocess: bool = True,
        include_classical: bool = True,
        include_quantum: bool = True,
        include_hybrid: bool = False
    ) -> pd.DataFrame:
        """
        Execute the complete research
        benchmark pipeline.

        Parameters
        ----------

        preprocess

            Whether to execute the
            preprocessing pipeline.

        include_classical

            Benchmark classical models.

        include_quantum

            Benchmark quantum models.

        include_hybrid

            Benchmark hybrid models.

        Returns
        -------

        pandas.DataFrame

            Unified research leaderboard.
        """

        # ----------------------------------
        # Preprocessing
        # ----------------------------------

        if preprocess:

            X, y = self.preprocess_dataset(

                X,

                y

            )

        # ----------------------------------
        # Containers
        # ----------------------------------

        classical_results = []

        quantum_results = []

        hybrid_results = []

        # ----------------------------------
        # Classical
        # ----------------------------------

        if include_classical:

            classical_results = (

                self.evaluate_classical(

                    X,

                    y

                )

            )

        # ----------------------------------
        # Quantum
        # ----------------------------------

        if include_quantum:

            quantum_results = (

                self.evaluate_quantum(

                    X,

                    y

                )

            )

        # ----------------------------------
        # Hybrid
        # ----------------------------------

        if include_hybrid:

            hybrid_results = (

                self.evaluate_hybrid(

                    X,

                    y

                )

            )

        # ----------------------------------
        # Merge Results
        # ----------------------------------

        leaderboard = self._merge_results(

            classical_results,

            quantum_results,

            hybrid_results

        )

        return leaderboard
    














    #Part 3



    # ======================================================
    # DISPLAY RESULTS
    # ======================================================

    def display_results(
        self,
        leaderboard: pd.DataFrame
    ) -> None:
        """
        Display the research leaderboard.
        """

        print()

        print("=" * 70)
        print("UNIFIED RESEARCH BENCHMARK RESULTS")
        print("=" * 70)

        if leaderboard.empty:

            print("\nNo benchmark results available.\n")
            return

        display_columns = [

            "rank",
            "category",
            "model",
            "accuracy",
            "accuracy_std",
            "f1"

        ]

        print(

            leaderboard[
                display_columns
            ].to_string(index=False)

        )

        print()

    # ======================================================
    # SAVE RESULTS
    # ======================================================

    def save_results(
        self,
        leaderboard: pd.DataFrame,
        dataset_name: str
    ) -> None:
        """
        Save benchmark results.
        """


        self.comparison_matrix.save_csv(
            leaderboard,
            dataset_name=dataset_name
        )

        

    # ======================================================
    # RESEARCH SUMMARY
    # ======================================================

    def print_summary(
        self,
        leaderboard: pd.DataFrame
    ) -> None:
        """
        Print a concise research summary.
        """

        if leaderboard.empty:

            return

        best_model = leaderboard.iloc[0]

        print()

        print("=" * 70)
        print("RESEARCH SUMMARY")
        print("=" * 70)

        print(
            f"Best Model      : {best_model['model']}"
        )

        print(
            f"Category        : {best_model['category']}"
        )

        print(
            f"Mean Accuracy   : "
            f"{best_model['accuracy']:.4f}"
        )

        print(
            f"Std Deviation   : "
            f"{best_model['accuracy_std']:.4f}"
        )

        print(
            f"F1 Score        : "
            f"{best_model['f1']:.4f}"
        )

        print()

    # ======================================================
    # COMPLETE PIPELINE
    # ======================================================

    def execute(
        self,
        X,
        y,
        dataset_name: str = "dataset"

    ) -> pd.DataFrame:
        """
        Execute the complete benchmark
        workflow.

        Steps

        1. Preprocess

        2. Benchmark

        3. Rank

        4. Display

        5. Save

        6. Return leaderboard
        """

        leaderboard = self.run(

            X,

            y,

            preprocess=True,

            include_classical=True,

            include_quantum=False,

            include_hybrid=False

        )

        leaderboard = self.comparison_matrix.generate(
            leaderboard.to_dict(
                orient="records"
            )
        )

        self.display_results(
            leaderboard
        )

        self.print_summary(
            leaderboard
        )

        self.save_results(

            leaderboard,

            dataset_name

        )

        return leaderboard

    # ======================================================
    # REPRESENTATION
    # ======================================================

    def __repr__(self):

        return (

            "ResearchBenchmark("

            f"classical={self.classical_registry.total_models()}, "

            f"quantum={self.quantum_registry.total_models()})"

        )
    




    