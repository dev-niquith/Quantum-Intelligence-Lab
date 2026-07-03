"""
quantum_registry.py

Quantum Intelligence Lab (QIL)

Central registry for all quantum
machine learning models.

Every new quantum model should be
registered here so that the benchmark
engine can discover it automatically.
"""

# ---------------------------------------------------------
# Quantum Models
# ---------------------------------------------------------

from src.models.quantum.vqc_model import VQCModel

# Future imports
#
# from src.models.quantum.estimator_qnn_model import (
#     EstimatorQNNModel
# )
#
# from src.models.quantum.sampler_qnn_model import (
#     SamplerQNNModel
# )
#
# from src.models.quantum.qsvc_model import (
#     QSVCModel
# )


class QuantumRegistry:
    """
    Registry responsible for managing all
    available quantum machine learning models.
    """

    def get_models(self):
        """
        Returns
        -------
        dict

            Dictionary mapping model names
            to instantiated models.
        """

        return {

            "VQC":
                VQCModel().build(),

            # Future Models
            #
            # "Estimator QNN":
            #     EstimatorQNNModel().build(),
            #
            # "Sampler QNN":
            #     SamplerQNNModel().build(),
            #
            # "QSVC":
            #     QSVCModel().build(),
        }

    def available_models(self):
        """
        Returns a list containing the names
        of all registered quantum models.
        """

        return list(
            self.get_models().keys()
        )

    def total_models(self):
        """
        Returns the total number of
        registered quantum models.
        """

        return len(
            self.get_models()
        )

    def __repr__(self):

        return (

            "QuantumRegistry("

            f"{self.total_models()} "

            "registered models)"

        )