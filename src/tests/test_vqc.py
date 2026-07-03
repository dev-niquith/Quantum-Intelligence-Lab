"""
test_vqc.py

Quantum Intelligence Lab (QIL)

Tests the Variational Quantum Classifier (VQC)
independently before integrating it into
the benchmarking engine.
"""

from sklearn.datasets import load_iris
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import accuracy_score

from src.models.quantum.vqc_model import VQCModel


def main():

    print("=" * 60)
    print("TEST : VARIATIONAL QUANTUM CLASSIFIER")
    print("=" * 60)

    # -------------------------------------------------
    # Load Dataset
    # -------------------------------------------------

    X, y = load_iris(return_X_y=True)

    # -------------------------------------------------
    # Binary Classification
    # -------------------------------------------------

    X = X[y != 2]

    y = y[y != 2]

    # -------------------------------------------------
    # Reduce Features
    # -------------------------------------------------

    X = PCA(
        n_components=2,
        random_state=42
    ).fit_transform(X)

    # -------------------------------------------------
    # Scale Features
    # -------------------------------------------------

    scaler = MinMaxScaler()

    X = scaler.fit_transform(X)

    # -------------------------------------------------
    # Train Test Split
    # -------------------------------------------------

    X_train, X_test, y_train, y_test = train_test_split(

        X,

        y,

        test_size=0.2,

        random_state=42,

        stratify=y

    )

    # -------------------------------------------------
    # Build Model
    # -------------------------------------------------

    print("\nBuilding VQC...\n")

    model = VQCModel().build()

    # -------------------------------------------------
    # Train
    # -------------------------------------------------

    print("Training...\n")

    model.fit(

        X_train,

        y_train

    )

    # -------------------------------------------------
    # Predict
    # -------------------------------------------------

    predictions = model.predict(

        X_test

    )

    accuracy = accuracy_score(

        y_test,

        predictions

    )

    print("=" * 60)

    print("VQC TEST SUCCESSFUL")

    print("=" * 60)

    print(f"Accuracy : {accuracy:.4f}")


if __name__ == "__main__":

    main()