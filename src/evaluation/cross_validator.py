"""
cross_validator.py

Quantum Intelligence Lab (QIL)

Research-grade Cross Validation Engine.

This module performs Stratified K-Fold Cross Validation
and computes evaluation metrics for every fold.

Why Stratified K-Fold?

Instead of evaluating a model using a single train/test split,
we train and evaluate the model multiple times using different
data splits. This produces much more reliable performance estimates.

Workflow

Dataset
    ↓
Cross Validation
    ↓
Preprocessing
    ↓
Model Training
    ↓
Prediction
    ↓
Metrics
    ↓
Statistical Analysis
"""

from typing import Dict

import numpy as np

from sklearn.base import clone
from sklearn.model_selection import StratifiedKFold

from src.evaluation.metrics_calculator import MetricsCalculator
from src.evaluation.statistical_analyzer import StatisticalAnalyzer
from src.preprocessing.preprocessing_pipeline import PreprocessingPipeline


class CrossValidator:
    """
    Research-grade Cross Validation Engine.
    """

    def __init__(
        self,
        folds: int = 5,
        random_seed: int = 42
    ):
        """
        Parameters
        ----------
        folds : int
            Number of folds.

        random_seed : int
            Seed for reproducibility.
        """

        self.folds = folds
        self.random_seed = random_seed

        self.metrics_calculator = MetricsCalculator()
        self.statistics = StatisticalAnalyzer()



    def _slice(self, data, indices):
        """
        Safely slice either a pandas DataFrame/Series
        or a NumPy array.

        Parameters
        ----------
        data
            Dataset or labels.

        indices
            Row indices.

        Returns
        -------
        Sliced data.
        """

        # pandas DataFrame / Series
        if hasattr(data, "iloc"):
            return data.iloc[indices]

        # NumPy array
        return data[indices]





    def evaluate(
        self,
        model,
        X,
        y
    ) -> Dict:
        """
        Evaluate a model using Stratified K-Fold Cross Validation.

        Parameters
        ----------
        model
            Any sklearn-compatible model.

        X
            Feature matrix.

        y
            Labels.

        Returns
        -------
        Dict

            Research evaluation report.
        """

        cv = StratifiedKFold(
            n_splits=self.folds,
            shuffle=True,
            random_state=self.random_seed
        )

        accuracy_scores = []
        precision_scores = []
        recall_scores = []
        f1_scores = []

        for fold_number, (train_index, test_index) in enumerate(cv.split(X, y), start=1):

            # ----------------------------------
            # Split Dataset
            # ----------------------------------
          

            def _slice(self, data, indices):
                """
                Slice either a pandas object or a NumPy array.

                Parameters
                ----------
                data
                    pandas DataFrame, pandas Series or NumPy array.

                indices
                    Row indices.

                Returns
                -------
                Sliced data.
                """

                if hasattr(data, "iloc"):
                    return data.iloc[indices]

                return data[indices]
            
            X_train = self._slice(X, train_index)
            X_test = self._slice(X, test_index)

            y_train = self._slice(y, train_index)
            y_test = self._slice(y, test_index)

            




































































            # ----------------------------------
            # Preprocessing
            # ----------------------------------

            pipeline = PreprocessingPipeline(
                k_features=15,
                pca_components=8
            )

            X_train = pipeline.fit_transform(
                X_train,
                y_train
            )

            X_test = pipeline.transform(
                X_test
            )

            # ----------------------------------
            # Fresh model for every fold
            # ----------------------------------

            current_model = clone(model)

            current_model.fit(
                X_train,
                y_train
            )

            predictions = current_model.predict(
                X_test
            )

            metrics = self.metrics_calculator.calculate(
                y_test,
                predictions
            )

            accuracy_scores.append(metrics["accuracy"])
            precision_scores.append(metrics["precision"])
            recall_scores.append(metrics["recall"])
            f1_scores.append(metrics["f1"])

        return {

            "accuracy": self.statistics.analyze(
                accuracy_scores
            ),

            "precision": self.statistics.analyze(
                precision_scores
            ),

            "recall": self.statistics.analyze(
                recall_scores
            ),

            "f1": self.statistics.analyze(
                f1_scores
            )

        }