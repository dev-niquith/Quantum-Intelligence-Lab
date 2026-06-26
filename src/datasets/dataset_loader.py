"""
dataset_loader.py

Purpose:
--------
Loads benchmark datasets used throughout QIL.

This file acts as the single entry point for all datasets.

Future:
--------
Later we can add:
- CSV uploads
- Kaggle datasets
- User datasets
- Quantum chemistry datasets
"""

from sklearn.datasets import (
    load_breast_cancer,
    load_iris,
    load_wine,
    load_digits
)

import pandas as pd


class DatasetLoader:
    """
    Responsible for loading datasets
    into a consistent format.

    Output:
    -------
    X -> Features DataFrame
    y -> Target Series
    """

    def load_dataset(self, dataset_name: str):

        dataset_name = dataset_name.lower()

        if dataset_name == "breast_cancer":
            dataset = load_breast_cancer()

        elif dataset_name == "iris":
            dataset = load_iris()

        elif dataset_name == "wine":
            dataset = load_wine()

        elif dataset_name == "digits":
            dataset = load_digits()

        else:
            raise ValueError(
                f"Dataset '{dataset_name}' not supported."
            )

        X = pd.DataFrame(
            dataset.data,
            columns=dataset.feature_names
        )

        y = pd.Series(
            dataset.target,
            name="target"
        )

        return X, y