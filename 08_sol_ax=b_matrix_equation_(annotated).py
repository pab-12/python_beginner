# NECESSARY PREREQUISITES

import numpy as np
from numpy.linalg import pinv

# The function below returns the solution of the matrix equation Ax=b when given the matrix A and the vector b as input.
# If there are infinite solutions, it will return the general solution, and if there are no solutions, it will return a blank array.

# The method uses a property of the Moore-Penrose pseudoinverse. See file 07(annotated).py for information on the fundamentals.

def general_solution(A, b):
    # See file 07(annotated).py for information on how the method finds how many solutions the equation has.
    Ap = pinv(A)
    m, n = A.shape
    
    if np.allclose((np.absolute(A @ Ap @ b - b)), np.zeros((n, n))):
        if np.allclose(Ap @ A, np.identity(n)):
            
            # Calculating the unique solution, which is given by x = Ap*b (as (In - Ap*A) = 0)
            x = [Ap @ b]
            return x
        
        else:
            
            # Calculating the general solution.
            # It is returned in the form of two separate arrays, c and N, where the solution is given by x = c + Nw with w being arbitrary.
            c = Ap @ b
            N = np.identity(m) - Ap @ A
            x = [c, N]
            return x
    else:
        # No solutions, so returns a blank array.
        x = []
        return x

# Replace the example matrix and vector below with your desired matrix and vector to find the solution.

Matrix_A = np.array([[3, 7, 4], [-3, -7, -4], [6, 14, 8]])
Vector_b = np.array([[2], [-2], [4]])

print(general_solution(Matrix_A, Vector_b))

