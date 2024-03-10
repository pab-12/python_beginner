import numpy as np

def f(x):
    return (6*x**3 + 5*np.exp(2*x)) / (4 * x)

x_data = np.arange(-10, 11)
fx_data = np.zeros(21)

for i in range(21):
     fx_data[i] = f(x_data[i])

print(x_data)
print(fx_data)

