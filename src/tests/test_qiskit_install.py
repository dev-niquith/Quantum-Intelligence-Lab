"""
test_qiskit_install.py

Verifies that the installed Qiskit environment
supports the components required by QIL.
"""

from qiskit.circuit.library import ZZFeatureMap
from qiskit.circuit.library import RealAmplitudes

from qiskit_machine_learning.algorithms import VQC

try:
    from qiskit.primitives import StatevectorSampler

    print("=" * 60)
    print("QISKIT INSTALLATION TEST")
    print("=" * 60)

    print("✓ ZZFeatureMap imported")

    print("✓ RealAmplitudes imported")

    print("✓ VQC imported")

    print("✓ StatevectorSampler imported")

    print("\nEverything looks good.")

except Exception as error:

    print("\nFAILED\n")

    print(error)