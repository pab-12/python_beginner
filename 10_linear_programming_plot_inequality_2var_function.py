import numpy as np
import matplotlib.pyplot as plt

def legend(a, b, inequality, c, x_axis, y_axis):
    leg_text = f'$'
    if a == 1:
        leg_text += f'~~'
    elif a == -1:
        leg_text += f'-'
    elif float(a).is_integer():
        leg_text += f'{a:4d}'
    else:
        leg_text += f'{a:.2f}'
    leg_text += x_axis
    if b == 1:
        leg_text += f'~ +~'
    elif b == -1:
        leg_text += f'-~'
    elif float(b).is_integer():
        leg_text += f'{b:+d}'
    else:
        leg_text += f'{b:+.2f}'
    leg_text += y_axis
    if float(c).is_integer():
        leg_text += f' = {c:d}$'
    else:
        leg_text += f' = {c:.2f}$'
    return leg_text

def plot_constraint(x_range, y_range, a, b, inequality, c, x_axis='x', y_axis='y'):
    plt.xlim(x_range)
    plt.ylim(y_range)
    x = np.linspace(x_range[0], x_range[1])
    leg_label = legend(a, b, inequality, c, x_axis, y_axis)
    
    if b != 0:
        y = (c - a * x) / b
        plt.plot(x, y, label=leg_label)
        if inequality == '<=':
            plt.gca().fill_between(x, y_range[0], np.maximum(y, y_range[0]), alpha=0.4)
        else:
            plt.gca().fill_between(x, np.maximum(y, y_range[0]), y_range[1], alpha=0.4)
    else:
        x.fill(c / a)
        y = np.linspace(y_range[0], y_range[1])
        plt.plot(x, y, label=leg_label)
        if inequality == '<=':
            plt.gca().fill_betweenx(y, x_range[0], np.maximum(c / a, x_range[0]), alpha=0.4)
        else:
            plt.gca().fill_betweenx(y, np.maximum(c / a, x_range[0]), x_range[1], alpha=0.4)
    plt.xlabel('$' + x_axis + '$')
    plt.ylabel('$' + y_axis + '$')
    plt.legend();

x_range = [-10, 10]
y_range = [-10, 10]
plot_constraint(x_range, y_range, 4.2, 5, '>=', -10)
plot_constraint(x_range, y_range, -0.46, 0, '<=', 2)
plt.show()

