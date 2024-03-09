import numpy as np
from numpy.linalg import pinv

def general_solution(A, b):
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

def test_general_solution(A, b):
    
    gen_sol_result = general_solution(A, b)
    m, n = A.shape
    
    if len(gen_sol_result) == 2:
        rng = np.random.default_rng()
        test_correct_count = 0
        
        for i in range(10):
            w = rng.random((n, 1))
            test_x = gen_sol_result[0] + gen_sol_result[1] @ w
            test = A @ test_x

            if np.allclose((np.absolute(test - b)), np.zeros((n, n))):
                test_correct_count = test_correct_count + 1
            
        return (test_correct_count == 10)
    
    elif len(gen_sol_result) == 1:
        test = A @ gen_sol_result[0]
        
        return np.allclose((np.absolute(test - b)), np.zeros((n, n)))
    
    else:
        test = A @ pinv(A) @ b
        
        return not np.allclose((np.absolute(test - b)), np.zeros((n, n)))

Matrix_A = np.array([[3, 7, 4], [-3, -7, -4], [6, 14, 8]])
Vector_b = np.array([[2], [-2], [4]])

print(general_solution(Matrix_A, Vector_b))
print()
print('Solution satisfied: ', test_general_solution(Matrix_A, Vector_b))

