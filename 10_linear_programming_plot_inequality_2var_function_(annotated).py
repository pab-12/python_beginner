# NECESSARY PREREQUISITES

import numpy as np
import matplotlib.pyplot as plt

# The function plot_inequality defined below is able to plot inequalities with two variables (ax + by <= c or ax + by => c, where a and b are real coefficients and c is a real constant) within a 
# given x-axis range and y-axis range, and will represent the area in which the inequalities hold by shading the areas with different colours.

# It has greatly assisted me in the solving of linear programming problems, as the visualisation of multiple inequalities and how they interact can aid in understanding how to tackle the problem.

# This first function lays the groundwork for the legend of the plot, and will be called later in the main function.

def legend(a, b, inequality, c, x_axis, y_axis):
    
    # Using f-string properties to generate the text for the legend.
    leg_text = f'$'

    # Modifying the string based on the properties of the a coefficient.
    if a == 1:
        leg_text += f'~~'
    elif a == -1:
        leg_text += f'-'
    elif float(a).is_integer():
        leg_text += f'{a:4d}'
    else:
        leg_text += f'{a:.2f}'
    leg_text += x_axis

    # Modifying the string based on the properties of the b coefficient.
    if b == 1:
        leg_text += f'~ +~'
    elif b == -1:
        leg_text += f'-~'
    elif float(b).is_integer():
        leg_text += f'{b:+d}'
    else:
        leg_text += f'{b:+.2f}'
    leg_text += y_axis

    # Adding the c value to the string.
    if float(c).is_integer():
        leg_text += f' = {c:d}$'
    else:
        leg_text += f' = {c:.2f}$'
    return leg_text


# Now, the main function. The parameter inequality takes only either >= or <=. The x_axis and y_axis labels can also be changed to display any two variables required.
# The x_range and y_range parameters each take a two-element array depicting the preferred plotting range. An example of all of these can be seen in the example provided below.


def plot_constraint(x_range, y_range, a, b, inequality, c, x_axis='x', y_axis='y'):
    # Starting by setting up the limitations of the plot, using the ranges provided.
    plt.xlim(x_range)
    plt.ylim(y_range)
    
    # Defining a range of equally spaced points across the x range.
    x = np.linspace(x_range[0], x_range[1])
    
    leg_label = legend(a, b, inequality, c, x_axis, y_axis)
    
    if b != 0:
        # Finding the corresponding y values for each of the x values generated previously.
        y = (c - a * x) / b
        plt.plot(x, y, label=leg_label)
        
        # As the above has plotted the line for the = case, now plotting the area to shade to represent the required inequality.
        # This is done by using the gca().fill_between function of matplotlib.pyplot, filling the area between the line and the upper or lower bounds of the initially
        # supplied range, depending on the inequality provided.
        if inequality == '<=':
            plt.gca().fill_between(x, y_range[0], np.maximum(y, y_range[0]), alpha=0.4)
        else:
            plt.gca().fill_between(x, np.maximum(y, y_range[0]), y_range[1], alpha=0.4)
    
    # In the case that an inequality with b=0 is entered, that is, the coefficient of the y value is 0, a straight line will be generated. This creates problems if the above
    # code is used to do this, so an exception needs to be established to handle inequalities of this nature.
    else:
        # Establishing the straight line and plotting. As all the x values will be the same, the .fill function is used to modify the x linspace to all the same value.
        x.fill(c / a)
        y = np.linspace(y_range[0], y_range[1])
        plt.plot(x, y, label=leg_label)
        
        # Again, now plotting the area to represent the inequality.
        if inequality == '<=':
            plt.gca().fill_betweenx(y, x_range[0], np.maximum(c / a, x_range[0]), alpha=0.4)
        else:
            plt.gca().fill_betweenx(y, np.maximum(c / a, x_range[0]), x_range[1], alpha=0.4)
    plt.xlabel('$' + x_axis + '$')
    plt.ylabel('$' + y_axis + '$')
    plt.legend();

# Now, establishing the ranges, and running the function.

x_range = [-10, 10]
y_range = [-10, 10]
plot_constraint(x_range, y_range, 4.2, 5, '>=', -10)
plot_constraint(x_range, y_range, -0.46, 0, '<=', 2)
plt.show()

