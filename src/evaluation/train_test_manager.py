"""
train_test_manager.py

Responsible for creating
consistent train-test splits.
"""

from sklearn.model_selection import (
    train_test_split
)


class TrainTestManager:

    def split(
        self,
        X,
        y,
        seed
    ):

        return train_test_split(

            X,

            y,

            test_size=0.2,

            random_state=seed,

            stratify=y
        )