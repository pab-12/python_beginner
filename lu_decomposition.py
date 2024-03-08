import numpy as np

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

X = np.array([[7, -18, 1], [34, 8, 4], [-27, -46, 18]])

L, U = LU_decompose(X)

print('X =')
print(A)
print()
print('L =')
print(L)
print()
print('U =')
print(U)

# Checking LU = X

print('Check: LU =')
print(L @ U)

