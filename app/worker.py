from qiskit import qasm3
from qiskit_aer import AerSimulator
import json

NUM_SHOTS = 1024

def execute_quantum_circuit(qasm3_string: str) -> dict:
    """
    Deserializes a QASM3 string, executes the quantum circuit, and returns the results.
    """
    try:
        # The QASM3 string is loaded and converted back into a QuantumCircuit object.
        qc = qasm3.loads(qasm3_string)

        # The circuit is executed on the AerSimulator.
        simulator = AerSimulator()
        job = simulator.run(qc, shots=NUM_SHOTS)
        result = job.result()
        counts = result.get_counts()

        return counts
    except Exception as e:
        # Log the error for debugging purposes.
        print(f"An error occurred during circuit execution: {e}")
        # Return a dictionary with an error message.
        return {"error": str(e)}