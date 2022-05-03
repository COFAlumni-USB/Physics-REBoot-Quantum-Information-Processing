#by Mauricio Gómez Viloria, 30 April 2022 for Physic REBoot 2022: Quantum information by COF Alumni USB

from qiskit import IBMQ, QuantumCircuit,execute,Aer
from qiskit.tools.monitor import job_monitor

dimension = input("\nChoose size of die 2^n with n=")
dimension= int(dimension)
if dimension>4:
    error
number_shots = input("\n How many shots? (from 1 to 8192)\n")
number_shots= int(number_shots)
if number_shots<1 or number_shots>8192:
    error

qc=QuantumCircuit(dimension)
qc.h(range(dimension))
qc.measure_all()
print(qc)

answer = input("Do you want to send it to IBM? (yes,no)\n")
if answer=='yes':
        print("\n")
        # IBMQ.save_account(TOKEN) #UNCOMMENT THIS LINE IF YOU HAVE NOT SAVED YOUR IBM ACCOUNT ON YOUR COMPUTER, ADD TOKEN
        IBMQ.load_account()
        provider=IBMQ.get_provider(hub='ibm-q')
        qcomp = provider.get_backend('ibmq_lima')
        job=execute(qc,backend=qcomp,shots=number_shots)
        print("\n")

        job_monitor(job) #to check on job
        result = job.result()
        
        counts=result.get_counts(qc)
        print("\n Results: \n")
        if dimension==2:
            print('Quantum Machine Learning team:',counts.get('01'),'\n')
            print('Quantum Algorithms team:',counts.get('10'),'\n')
            print('Error mitigation team:',counts.get('11'))
        else:
            print(counts)
        print("\n")
elif answer=='no':
        print("\n")
        qcomp = Aer.get_backend('qasm_simulator')
        job=execute(qc,backend=qcomp,shots=number_shots)
        print("\n")

        job_monitor(job) #to check on job
        result = job.result()
        if dimension==2:
            counts=result.get_counts(qc)
            print("\n Results:\n")
            print('Equipo 1:',counts.get('01'),'\n')
            print('Equipo 2:',counts.get('10'),'\n')
            print('Equipo 3:',counts.get('11'))
        else:
            print(counts)
        print("\n")
