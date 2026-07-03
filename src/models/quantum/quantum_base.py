"""
quantum_base.py

Quantum Intelligence Lab (QIL)

Base interface for all quantum machine learning models.

Every quantum model implemented inside QIL should inherit
from this class.

Examples
--------
QSVM

VQC

EstimatorQNN

SamplerQNN

Future quantum models should implement the methods defined
below to ensure a consistent interface throughout the
benchmarking engine.
"""

from abc import ABC, abstractmethod


class QuantumBaseModel(ABC):
    """
    Abstract base class for all quantum models.
    """

    def __init__(self):

        self.model_name = self.__class__.__name__

        self.model_type = "Quantum"

    @abstractmethod
    def build(self):
        """
        Build and return the quantum model.

        Returns
        -------
        object
            Instantiated quantum machine learning model.
        """
        pass

    def get_name(self):
        """
        Returns the display name of the model.
        """

        return self.model_name

    def get_type(self):
        """
        Returns the model category.
        """

        return self.model_type

    def info(self):
        """
        Returns metadata describing the model.
        """

        return {

            "name": self.get_name(),

            "type": self.get_type()

        }

    def __repr__(self):

        return (

            f"{self.model_name}"

            f"(type={self.model_type})"

        )