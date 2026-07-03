# IMPORT DEPENDENCIES
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram 
import matplotlib.pyplot as plt

# Create a Quantum Circuit with 2 qubits and 2 classical bits
qc = QuantumCircuit(2, 2)

# Create a Bell state (entanglement) using a Hadamard and a CNOT gate
qc.h(0)
qc.cx(0, 1)

# Measure all qubits into their corresponding classical bits
qc.measure([0, 1], [0, 1])


# Initialize the Aer simulator and execute the circuit for 1024 shots
simulator = AerSimulator()
result = simulator.run(
    qc,
    shots=1024
).result()

# Gather the resulting measurement counts
counts = result.get_counts()

# Print raw text counts and plot the histogram data
print(counts)
plot_histogram(counts) 
plt.show()