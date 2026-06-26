"""
dataset_profiler.py

Purpose:
--------
Generate statistical information
about a dataset.

Used by:
---------
- Dataset Intelligence Layer
- Recommendation Engine
- Benchmark Engine
"""

import numpy as np


class DatasetProfiler:

    def profile(self, X, y):

        profile = {
            "num_samples": len(X),
            "num_features": X.shape[1],
            "num_classes": y.nunique(),
            "missing_values": int(X.isnull().sum().sum()),
            "class_distribution": y.value_counts().to_dict(),
        }

        return profile