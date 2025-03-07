# Quantum Computing Simulations with Qiskit

This project contains Python programs that simulate basic quantum operations using **Qiskit**, a quantum computing framework. It demonstrates quantum entanglement and single-qubit operations.

## Files and Functionality

### 1️⃣ `entangle.py`
- Creates a **Bell pair** (entangled qubits) using:
  - **Hadamard gate (H)** to put the first qubit in superposition.
  - **CNOT gate (CX)** to entangle it with the second qubit.
- Measures the qubits and visualizes the probability distribution.
- Uses the `qasm_simulator` to execute the quantum circuit.
- **Output:** A histogram showing measurement results.

🔹 **Run it:**
```sh
python entangle.py
2️⃣ quibt.py

    Creates a single qubit state and applies an X (NOT) gate.
    Uses the statevector_simulator to analyze the quantum state after applying the gate.
    Output: Prints the quantum state vector.

🔹 Run it:

python quibt.py

Requirements

Ensure you have Qiskit installed before running the scripts:

pip install qiskit matplotlib

Concepts Covered

✅ Quantum Entanglement
✅ Qubit State Manipulation
✅ Qiskit Simulation
