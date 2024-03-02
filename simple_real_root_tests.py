# NECESSARY PREREQUISITES

import numpy as np

# Given a quadratic equation ax^2 + bx + c = 0 (where a, b and c are real and a is non-zero) and, by using the determinant:

# The fuction defined below finds and prints the number of real roots of the quadratic equation.

def count_roots(a, b, c):
    Δ = b ** 2 - 4 * a * c
    # Above, Δ stands for the determinant of the quadratic.
    if Δ == 0:
        print("There is only one real root to this quadratic")
    elif Δ < 0:
        print("There are no real roots to this quadratic")
    else:
        print("There are two real roots to this quadratic")


# The fuction defined below finds and prints the real roots of the quadratic equation if it has any.

def value_roots(a, b, c):
    Δ = b ** 2 - 4 * a * c
    # Above, Δ stands for the determinant of the quadratic.
    if Δ == 0:
        sol = (-b)/(2 * a)
        print("There is only one real root to this quadratic, which is ", sol)
    elif Δ < 0:
        print("There are no real roots to this quadratic")
    else:
        pos_sol = (-b + np.sqrt(Δ))/(2 * a)
        neg_sol = (-b - np.sqrt(Δ))/(2 * a)
        lroot = max(pos_sol, neg_sol)
        sroot = min(pos_sol, neg_sol)
        print(f"There are two real roots to this quadratic")
        print("The larger real root of this quadratic is ", lroot)
        print(f"The smaller real root of this quadratic is ", sroot)
