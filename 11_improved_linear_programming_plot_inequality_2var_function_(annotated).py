# NECESSARY PREREQUISITES

import numpy as np
import matplotlib.pyplot as plt

# The function plot_inequality defined below is an improved version of the function described in file 10(annotated).py, which modifies the function so that it can
# plot the strict < and > inequalities too, in addition to =< and =>.
# The annotations on this file will only cover the changes added, see file 10(annotated).py for details on the rest of the code.

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
    
    # Adding an extra if statement here to ensure if the inequality is a strict inequality, the legend will appropriately describe the line drawn as a not equal to (≠) line.
    if inequality == '<=' or inequality == '>=':
        leg_text += f' ='
    else:
        leg_text += f' ≠'
    
    if float(c).is_integer():
        leg_text += f' {c:d}$'
    else:
        leg_text += f' {c:.2f}$'
    return leg_text

def plot_constraint(x_range, y_range, a, b, inequality, c, x_axis='x', y_axis='y'):
    plt.xlim(x_range)
    plt.ylim(y_range)
    x = np.linspace(x_range[0], x_range[1])
    leg_label = legend(a, b, inequality, c, x_axis, y_axis)
    
    if b != 0:
        y = (c - a * x) / b
        
        # Here, an if statement is added to cover the other 2 inequalities. For these, the line will be drawn as a dashed line, to represent
        # the strict inequality - showing that the points on the line are not included in the region.
        if inequality == '<=' or inequality == '>=':
            plt.plot(x, y, label=leg_label)
            if inequality == '<=':
                plt.gca().fill_between(x, y_range[0], np.maximum(y, y_range[0]), alpha=0.4)
            else:
                plt.gca().fill_between(x, np.maximum(y, y_range[0]), y_range[1], alpha=0.4)
        else:
            plt.plot(x, y, '--', label=leg_label)
            if inequality == '<':
                plt.gca().fill_between(x, y_range[0], np.maximum(y, y_range[0]), alpha=0.4)
            else:
                plt.gca().fill_between(x, np.maximum(y, y_range[0]), y_range[1], alpha=0.4)
       
    else:
        x.fill(c / a)
        y = np.linspace(y_range[0], y_range[1])
        
        # Doing the same as above to this part of the function too.
        if inequality == '<=' or inequality == '>=':
            plt.plot(x, y, label=leg_label)
            if inequality == '<=':
                plt.gca().fill_betweenx(y, x_range[0], np.maximum(c / a, x_range[0]), alpha=0.4)
            else:
                plt.gca().fill_betweenx(y, np.maximum(c / a, x_range[0]), x_range[1], alpha=0.4)
        else:
            plt.plot(x, y, '--', label=leg_label)
            if inequality == '<':
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
plot_constraint(x_range, y_range, 1, 2.1, '>', -2.85)
plt.show()

