# NECESSARY PREREQUISITES

import numpy as np
from numpy.linalg import norm

# The optional prerequisite below makes the iterations more readable, as it supresses the scientific notation of very large/small numbers.
np.set_printoptions(suppress=True)

# First, defining the LU decomposition. See lu_decomposition_(annotated).py in the repository for information.

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

# The function below uses the LR iterative method to attempt to find the real eigenvalues of any given square matrix.

def LR_eigenvalues(M, max_iterations=500, tol=1e-10, verbose=False):
    A = np.array(M)
    for i in range(max_iterations):
        
        # The decomposition is performed on loop, with a new A each time.
        
        L, U = LU_decompose(A)
        
        # This is the segment that allows the iterations to be printed if verbose=True.
        
        if verbose:
            print(f'Iteration {i + 1}, L=')
            print(L)
            print('U =')
            print(U)
            print()
            
        # Here it is checking, using the numpy norm function, that the norm (of infinite order) of the difference between the diagonals of the U and
        # the previous iteration's U is lower than the tol value stated, and if so, returns the diagonal of U as the eigenvalues of the matrix M supplied.
        
        if i > 0 and norm(np.diagonal(U) - U_diag_previous, np.inf) < tol:  
            return np.diagonal(U), i+1
        
        # If not, then the old U is refreshed to be the current U, and A is reformed from the L and the current U, ready to be LU decomposed again.
        
        U_diag_previous = np.diagonal(U)
        A = U @ L
        
    return 'Unsuccessful. Max iterations reached before eigenvalues found.', i+1

# Replace the square matrix X below with the square matrix you wish to find the real eigenvalues of.

X = np.array([[1, 2, -3, 8, 3],
              [0, 1, 0, 3, 0],
              [0, 2, 1, 6, -1],
              [6, -3, 0, 5, 2],
              [2, 1, 2, 3, -4]])

# Adjust the parameters here if you wish. The default values are stated in the function definition above.
# - Increase the max iterations if the limit is reached too early, and decrease the tol value for higher precision.
# - Generally, the lower the tol value, the more iterations needed to find the eigenvalues.
# - Setting verbose to True will print the iteration at each stage.

e = LR_eigenvalues(X)

print('Eigenvalues:', e[0])
print('Number of iterations:', e[1])

# If still unsuccessful after repeating adjusting of parameters, the method may not be suitable to find the real eigenvalues of that particular square matrix.
# For example, if the square matrix has any complex eigenvalues, there will be issues.

