"""
vqc_model.py

Quantum Intelligence Lab (QIL)

Variational Quantum Classifier (VQC)

This module builds a VQC model using
Qiskit Machine Learning.

Architecture

Feature Map
        ↓
Variational Ansatz
        ↓
VQC Classifier
"""

from qiskit.circuit.library import ZZFeatureMap
from qiskit.circuit.library import RealAmplitudes

from qiskit.primitives import StatevectorSampler

from qiskit_machine_learning.algorithms import VQC

from src.models.quantum.quantum_base import (
    QuantumBaseModel
)


class VQCModel(QuantumBaseModel):
    """
    Variational Quantum Classifier.
    """

    def __init__(self):

        super().__init__()

        self.model_name = "VQC"

    def build(self):
        """
        Build and return a VQC model.
        """

        # ----------------------------------
        # Number of input features
        # ----------------------------------

        num_features = 2

        # ----------------------------------
        # Feature Map
        # ----------------------------------

        feature_map = ZZFeatureMap(

            feature_dimension=num_features,

            reps=2

        )

        # ----------------------------------
        # Variational Circuit
        # ----------------------------------

        ansatz = RealAmplitudes(

            num_qubits=num_features,

            reps=2

        )

        # ----------------------------------
        # Quantum Sampler
        # ----------------------------------

        sampler = StatevectorSampler()

        # ----------------------------------
        # Build VQC
        # ----------------------------------

        model = VQC(

            sampler=sampler,

            feature_map=feature_map,

            ansatz=ansatz

        )

        return model