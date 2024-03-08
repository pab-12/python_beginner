# NECESSARY PREREQUISITES

import numpy as np

# The function below finds the lower-upper (LU) decomposition of any square matrix, returning the lower and upper triangular matrices upon execution.

def LU_decompose(A):
    m, n = A.shape

    # The below assert check is to ensure that the matrix supplied is a square matrix, otherwise the method won’t work.
    assert m == n, 'lu_decompose cannot be performed with a non-square array'
    
    # Initializing the L and U arrays
    L = np.zeros_like(A, dtype=float)
    U = np.zeros_like(A, dtype=float)

    # Now, performing the calculations
    for j in range(0, n):
        # Creating the lower diagonal matrix (U)
        for i in range(0, j + 1):
            U[i, j] = A[i, j] - L[i, :i] @ U[:i, j]
        # Creating the upper diagonal matrix (L)
        for i in range(j + 1, n):
            L[i, j] = (A[i, j] - L[i, :j] @ U[:j, j]) / U[j, j]

    # Finalizing the creation of the L matrix
    np.fill_diagonal(L, 1)

    return L, U

# Replace the array A below with your desired matrix to be LU decomposed.

A = np.array([[7, -18, 1], [34, 8, 4], [-27, -46, 18]])

L, U = LU_decompose(A)

print('A =')
print(A)
print()
print('L =')
print(L)
print()
print('U =')
print(U)

# A check can be performed after the calculation. If the decomposition has been successful, then L * U = A, by definition. Therefore:

print('Check: LU =')
print(L @ U)

