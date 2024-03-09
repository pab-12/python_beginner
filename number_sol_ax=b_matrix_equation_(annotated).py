# NECESSARY PREREQUISITES

import numpy as np
from numpy.linalg import pinv

# The function below returns the number of solutions of the matrix equation Ax=b when given the matrix A and the vector b as input.
# It uses one of the fundemental properties of the Moore-Penrose pseudoinverse, that is, where Ap is the pseudoinverse;
# Ax = b has a solution if and only if A*Ap*b = b, and if so, then x = Ap*b + (I- Ap*A)w, where w is arbitrary.

def number_of_solutions(A, b):
    
    # The pinv function returns the moore-penrose pseudo-inverse using the SVD (singular value decomposition).
    Ap = pinv(A)
    
    # Assigning the dimensions of A
    m, n = A.shape
    
    # As allclose only deals with positive values when it comes to the tolerance, the if statement below takes the absolute of the resulting A*Ap*b - b matrix
    # to compare to the zero matrix.
    # So, given the fact that if A*Ap*b != b then Ax = b has no solutions, then
    if np.allclose((np.absolute(A @ Ap @ b - b)), np.zeros((n, n))):
        
        # The next condition is that if Ap*A = In, then there is 1 unique solution, and if not, then there is a general solution for Ax = b
        # that gives an infinite number of solutions, so
        if np.allclose(Ap @ A, np.identity(n)):
            return 1
        else:
            return 'infinite solutions'
    else:
        return 0

# Replace the example matrix and vector below with your desired matrix and vector to find the number of solutions.

Matrix_A = np.array([[3, 7, 4], [-3, -7, -4], [6, 14, 8]])
Vector_b = np.array([[2], [-2], [4]])

print(number_of_solutions(Matrix_A, Vector_b))

