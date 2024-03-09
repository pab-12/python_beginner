import numpy as np
from numpy.linalg import pinv

def number_of_solutions(A, b):
    Ap = pinv(A)
    m, n = A.shape
    
    if np.allclose((np.absolute(A @ Ap @ b - b)), np.zeros((n, n))):
        if np.allclose(Ap @ A, np.identity(n)):
            x = [Ap @ b]
            return x
        else:
            c = Ap @ b
            N = np.identity(m) - Ap @ A
            x = [c, N]
            return x
    else:
        x = []
        return x

Matrix_A = np.array([[3, 7, 4], [-3, -7, -4], [6, 14, 8]])
Vector_b = np.array([[2], [-2], [4]])

print(number_of_solutions(Matrix_A, Vector_b))

