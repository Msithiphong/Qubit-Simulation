from qiskit import QuantumCircuit, transpile
from qiskit_aer import Aer
from qiskit.visualization import plot_histogram

qc = QuantumCircuit(1)

qc.x(0)

simulator = Aer.get_backend('statevector_simulator')

compiled_circuit = transpile(qc, simulator)

job = simulator.run(compiled_circuit)
result = job.result()

statevector = result.get_statevector()
print(statevector)