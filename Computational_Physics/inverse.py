import numpy as np
import sympy as sp
A=np.array([[1,2,3],[2,3,1],[3,1,2]])
B=np.array([[5],[6],[7]])
D=np.dot(A,B)
D=A.transpose()
D=np.linalg.inv(A)
print(D)

import numpy as np

A = np.array([[1,2,3],[2,3,1],[3,1,2]])

A_inv = np.linalg.inv(A)
print(A_inv)
