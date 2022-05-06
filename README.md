# What is Pulse Gate?

Sending direct schedules to IBM Quantum backends is now deprecated. Modern method employs the use of Pulse Gate. In short, we are now able to calibrate an arbitrarily defined unitary gate in a specific circuit, using pulse schedules in which we can use [Pulse Builder](https://qiskit.org/documentation/apidoc/pulse.html#pulse-builder) to write pulse programs. 

# Why this repository?

Concomitant with the emergence of Pulse Gate is the need to reproduce imperative experiments for further quantum computing research, namely Rabi oscillation, discrimination of computational eigenstates, and dynamical coupling. Written in accordance with standard Pulse Gate syntax, this repo hosts a variety of Jupyter notebooks that reproduced some of these important experiments that serve as cheatsheets for Qiskit users. 

# References

1. [Qiskit Textbook](https://qiskit.org/textbook/ch-quantum-hardware/calibrating-qubits-pulse.html)
2. [qiskit-community-tutorials/2022-04-12-armonk-retirement-pulse](https://github.com/qiskit-community/qiskit-community-tutorials/blob/master/video-companions/2022-04-12-armonk-retirement-pulse/armonk-to-pulse-gates.ipynb)


