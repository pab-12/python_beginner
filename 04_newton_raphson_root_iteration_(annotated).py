# NECESSARY PREREQUISITES

import numpy as np

# The code below uses the Newton-Rhapson iteration method to attempt to find a root of f(x) = 0 for any given f(x).
# If there is more than one root of f(x) = 0, the found root will depend on the initial value supplied.
 
# First, replace the example expressions below with the desired f(x) and f'(x).

def f(x):
    return 2*x**2 + 5*np.sin(2*x) - 6

def f_prime(x):
    return 4*x - np.cos(2*x)

# Now, defining the method:

def g(x):
    return x - f(x) / f_prime(x)

def newton_raphson(x0, 𝜖=1e-10, max_iterations=100):
    r = 0
    xr = x0
    xr_plus1 = g(xr)
    
    while abs(xr_plus1 - xr) > 𝜖 and r < max_iterations:
        r = r + 1
        xr = xr_plus1
        xr_plus1 = g(xr)
    
    return xr_plus1, abs(xr_plus1 - xr), r+1

# To perform the method, replace the elements in the function below with the desired parameters, a being the starting value for the iteration,
# b being the tolerance value determining how precise the result will be, and c being the max number of iterations before the method stops, even before finding a root.

# (If unsure, exclude the second and third elements, which will result in the function using the default recommended settings, the tolerance value 𝜖 = 1e-10 and the max iterations = 100.)

result = newton_raphson(a, b, c)

print('root = {}, absolute error = {}, number of iterations = {}'.format(result[0], result[1], result[2]))

# If there are issues, try adjusting the starting value, considering these points:
#  - Starting values very far away from the root(s) can cause the method to diverge.
#  - Selecting stationary values (where f'(x0) = 0) will cause issues.

# There are multiple other reasons the Newton-Rhapson method can be ineffective. If there are still issues after adjusting the starting value a number of times, I would look into
# the behaviour of the function and how the method works, and assess if the Newton-Rhapson method would be an effective method for finding the roots in that particular case.

