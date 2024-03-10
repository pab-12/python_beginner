import numpy as np
from numpy.linalg import norm
np.set_printoptions(suppress=True)

def LU_decompose(A):
    m, n = A.shape
    
    assert m == n, 'lu_decompose cannot be performed with a non-square array'
    
    L = np.zeros_like(A, dtype=float)
    U = np.zeros_like(A, dtype=float)
    
    for j in range(0, n):
        for i in range(0, j + 1):
            U[i, j] = A[i, j] - L[i, :i] @ U[:i, j]
        for i in range(j + 1, n):
            L[i, j] = (A[i, j] - L[i, :j] @ U[:j, j]) / U[j, j]
            
    np.fill_diagonal(L, 1)
    
    return L, U

def LR_eigenvalues(M, max_iterations=500, tol=1e-10, verbose=False):
    A = np.array(M)
    for i in range(max_iterations):
        L, U = LU_decompose(A)
        if verbose:
            print(f'Iteration {i + 1}, L=')
            print(L)
            print('U =')
            print(U)
            print()
        if i > 0 and norm(np.diagonal(U) - U_diag_previous, np.inf) < tol:  
            return np.diagonal(U), i+1
        U_diag_previous = np.diagonal(U)
        A = U @ L
    return 'Unsuccessful. Max iterations reached before eigenvalues found.', i+1


X = np.array([[1, 2, -3, 8, 3],
              [0, 1, 0, 3, 0],
              [0, 2, 1, 6, -1],
              [6, -3, 0, 5, 2],
              [2, 1, 2, 3, -4]])

e = LR_eigenvalues(X)

print('Eigenvalues:', e[0])
print('Number of iterations:', e[1])

