import qiskit
import math
from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, execute, BasicAer, IBMQ
#from qiskit.providers.ibmq import least_busy

qr = qiskit.QuantumRegister(2)
cr = qiskit.ClassicalRegister(2)
qc = qiskit.QuantumCircuit(qr, cr)

qc.measure(qr[0], cr[0])
qc.measure(qr[1], cr[1])

backend = qiskit.BasicAer.get_backend('qasm_simulator')
job1 = qiskit.execute([qc], backend=backend, shots=1000)
result1 = job1.result()

print(result1.get_counts(qc))

qc.h(qr[0])

qc.cx(qr[0], qr[1])

token = "TOKEN"
IBMQ.save_account(token, overwrite=True)
IBMQ.load_account()

#backend = least_busy(IBMQ.backends())