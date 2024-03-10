import numpy as np

def f(x):
    return 2*x**2 + 5*np.sin(2*x) - 6

def f_prime(x):
    return 4*x - np.cos(2*x)

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

result = newton_raphson(a, b, c)
print('root = {}, absolute error = {}, number of iterations = {}'.format(result[0], result[1], result[2]))

