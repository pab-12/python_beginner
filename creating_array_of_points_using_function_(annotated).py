# NECESSARY PREREQUISITES

import numpy as np

# The code below is a quick way of applying a function to an array of x values, and creating an array of corresponding f(x) results.
# First, state the function

def f(x):
    return (6*x**3 + 5*np.exp(2*x)) / (4 * x)

# Then, forming the arrays, say for instance we would like a range of f(x) values for -10 <= x <= 10, where x is an integer

x_data = np.arange(-10, 11)

# Next, initialising the results array (size of 21 below as we want all the results from -10 to 10, INCLUDING 0)

fx_data = np.zeros(21)

# With this, now applying the function
 
for i in range(21):
     fx_data[i] = f(x_data[i])

print(x_data)
print(fx_data)

