"""
base_model.py

Quantum Intelligence Lab (QIL)

Defines the abstract base class for every model used within QIL.

All Classical, Quantum and Hybrid models inherit from this class,
ensuring that every model follows a common interface.

Benefits
--------
• Consistent API
• Easy benchmarking
• Plug-and-play architecture
• Future extensibility
"""

from abc import ABC, abstractmethod


class BaseModel(ABC):
    """
    Abstract base class for every model in QIL.
    """

    def __init__(self, model_name: str):

        self._model_name = model_name

    @property
    def name(self) -> str:
        """
        Returns the human-readable model name.
        """

        return self._model_name

    @property
    def category(self) -> str:
        """
        Model category.

        Override in subclasses if necessary.

        Returns
        -------
        str
        """

        return "Unknown"

    @abstractmethod
    def build(self):
        """
        Construct and return the underlying model.

        Returns
        -------
        object
            A fully initialized machine learning model.
        """
        pass

    def get_metadata(self) -> dict:
        """
        Returns metadata describing the model.

        This method can be extended by subclasses to include
        additional information such as:

        • Hyperparameters
        • Number of Qubits
        • Backend
        • Feature Map
        • Ansatz
        • Optimizer

        Returns
        -------
        dict
        """

        return {

            "name": self.name,

            "category": self.category

        }

    def __repr__(self):

        return (
            f"{self.__class__.__name__}"
            f"(name='{self.name}', "
            f"category='{self.category}')"
        )