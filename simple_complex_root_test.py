import numpy as np

def value_roots(a, b, c):
    Δ = b ** 2 - 4 * a * c
    if Δ == 0:
        sol = (-b)/(2 * a)
        print("There is only one real root to this quadratic, which is ", sol)
    elif Δ < 0:
        pos_sol = (-b + np.emath.sqrt(Δ))/(2 * a)
        neg_sol = (-b - np.emath.sqrt(Δ))/(2 * a)
        print("There are no real roots to this quadratic, so the two distint imaginary roots (that are complex conjugates of eachother) are")
        print(pos_sol)
        print("and")
        print(neg_sol)
    else:
        pos_sol = (-b + np.sqrt(Δ))/(2 * a)
        neg_sol = (-b - np.sqrt(Δ))/(2 * a)
        lroot = max(pos_sol, neg_sol)
        sroot = min(pos_sol, neg_sol)
        print(f"There are two real roots to this quadratic")
        print(f"The larger real root of this quadratic is ", lroot)
        print(f"The smaller real root of this quadratic is ", sroot)

 