#from qiskit import QuantumCircuit
from qiskit import QuantumCircuit, Aer, execute
from qiskit.visualization import plot_bloch_multivector, plot_histogram
from mpl_toolkits import mplot3d
from math import sqrt
from histograms import histograms
import numpy as np

qc = QuantumCircuit(1)

# Define initial_state as |1⟩
initial_state = [0, 1]

# Apply initialization operation to the qubit at position 0
qc.initialize(initial_state, 0)

qc.x(0)
qc.h(0)

out = execute(qc,Aer.get_backend('statevector_simulator')).result().get_statevector()

plot_bloch_multivector(out)

qc.measure_all()

results = execute(qc,Aer.get_backend('qasm_simulator')).result().get_counts()

plot_histogram(results)

qc.draw(output='mpl')

qc = QuantumCircuit(1)

initial_state = [1/sqrt(2), 1/sqrt(2)]

qc.initialize(initial_state, 0)