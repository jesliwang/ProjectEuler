import os, sys

# https://www.alpertron.com.ar/QUAD.HTM
# Diophantine Quadratic Equation


# x^2 + 41*x = 2*y^2+58*y
def solve_100(begin):
    n = 85
    m = 120

    while m < begin:
        nextN = -3*n - 2*m + 2
        nextM = -4*n - 3*m + 3

        n = abs(nextN)
        m = abs(nextM)

    print n, m
    return m

print solve_100(pow(10,12))
