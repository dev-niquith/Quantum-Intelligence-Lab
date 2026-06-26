"""
seed_manager.py

Responsible for reproducibility.
"""

import random
import numpy as np


class SeedManager:

    @staticmethod
    def set_seed(seed):

        random.seed(seed)

        np.random.seed(seed)