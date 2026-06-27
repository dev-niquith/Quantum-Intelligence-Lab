"""
test_preprocessing.py

Verify preprocessing pipeline.
"""

from src.datasets.dataset_loader import (
    DatasetLoader
)

from src.preprocessing.preprocessing_pipeline import (
    PreprocessingPipeline
)


loader = DatasetLoader()

X, y = loader.load_dataset(
    "breast_cancer"
)

print(
    "\nOriginal Shape:",
    X.shape
)

pipeline = (
    PreprocessingPipeline(
        k_features=15,
        pca_components=8
    )
)

X_processed = (
    pipeline.fit_transform(
        X,
        y
    )
)

print(
    "Processed Shape:",
    X_processed.shape
)