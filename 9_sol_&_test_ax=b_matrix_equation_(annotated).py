# NECESSARY PREREQUISITES

import numpy as np
from numpy.linalg import pinv

# The purpose of this code is to test whether the solution found using the function from sol_ax=b_matrix_equation.py is correct or not.
# First, importing the general solution function. See sol_ax=b_matrix_equation_(annotated).py and number_ sol_ax=b_matrix_equation_(annotated).py
# for more information on the function and usage of the Moore-Penrose pseudoinverse.

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
    
# Now, defining a new function, which takes the A matrix and b vector as input, calculates the solution result internally
# and then tests it to see if it is correct, returning True if the solution satisfies or False if it does not.

def test_general_solution(A, b):
    
    gen_sol_result = general_solution(A, b)
    m, n = A.shape
    
    # Sorting the general_solution results, using the fact that an Ax = b with infinite solutions returns a 2 element array from general_solution.
    if len(gen_sol_result) == 2:
        
        # Using a random number generator to define an arbitrary w (as the general solution is x = c + Nw for arbitrary w, see
        # sol_ax=b_matrix_equation_(annotated).py for more information).
        rng = np.random.default_rng()
        test_correct_count = 0
        
        # The below for loop tests 10 different arbitrary w vectors and only confirms the solution is correct if all 10 w tests pass.
        for i in range(10):
            
            # Defining w with the rng generator as a vector with length equal to the width of A.
            w = rng.random((n, 1))
            
            # Below we have x = c + Nw
            test_x = gen_sol_result[0] + gen_sol_result[1] @ w
            # Now, checking this x value satisfies Ax = b
            test = A @ test_x
            
            # As allclose only deals with positive values when it comes to the tolerance, the if statement below takes the absolute of the 
            # resulting test - b matrix to compare to the zero matrix.
            if np.allclose((np.absolute(test - b)), np.zeros((n, n))):
                test_correct_count = test_correct_count + 1
            
        return (test_correct_count == 10)
        
    # The same as before, except checking for a 1 element array, which is what is returned by an Ax = b with 1 unique solution.
    elif len(gen_sol_result) == 1:
        
        # Checking this x value satisfies Ax = b
        test = A @ gen_sol_result[0]
        
        return np.allclose((np.absolute(test - b)), np.zeros((n, n)))
    
    # And finally, dealing with the empty array, that is, when Ax = b has no solutions.
    else:
        
        # By the definition of the Moore-Penrose pseudoinverse property used to find the general solution, Ax = b has a solution if and only if
        # A*Ap*b = b. So, if this is false, then the equation is proven to have no solutions.
        test = A @ pinv(A) @ b
        
        return not np.allclose((np.absolute(test - b)), np.zeros((n, n)))

# Replace the example matrix and vector below with your desired matrix and vector to find the solution and to test if it is correct.

Matrix_A = np.array([[3, 7, 4], [-3, -7, -4], [6, 14, 8]])
Vector_b = np.array([[2], [-2], [4]])

print(general_solution(Matrix_A, Vector_b))
print()
print('Solution satisfied: ', test_general_solution(Matrix_A, Vector_b))

# For this final function regarding the Moore-Penrose pseudoinverse work, I will include a few other arrays that are proven to work with
# this code below. These will not be present on the unannotated version.

Example_Matrix_A1 = np.array([[1, 1, 2], [3, 7, 4], [4, 8, 6]])
Example_Vector_b1 = np.array([[2], [2], [4]])
Example_Matrix_A2 = np.array([[1, 1, 2], [3, 7, 4], [4, 8, 6]])
Example_Vector_b2 = np.array([[1], [1], [1]])
Example_Matrix_A3 = np.array([[1, 1, 2], [3, 4, 7], [4, 5, 4]])
Example_Vector_b3 = np.array([[1], [1], [11]])

print()
print()
print('--------------- Extra example Ax = b equations --------------')
print()
print(general_solution(Example_Matrix_A1, Example_Vector_b1))
print()
print('Solution satisfied: ', test_general_solution(Example_Matrix_A1, Example_Vector_b1))
print()
print(general_solution(Example_Matrix_A2, Example_Vector_b2))
print()
print('Solution satisfied: ', test_general_solution(Example_Matrix_A2, Example_Vector_b2))
print()
print(general_solution(Example_Matrix_A3, Example_Vector_b3))
print()
print('Solution satisfied: ', test_general_solution(Example_Matrix_A3, Example_Vector_b3))
print()

