from engine import evaluate
import math
from astsolver import *

def solve_linear(a, b):
    # Here, 'a' is the coefficient of x, and 'b' is the constant
    if a == 0:
        if b == 0:
            return "Infinite solutions"
        return "No solution"
    x = -b / a
    return f"x = {round(x, 10)}" # Added rounding for GitHub polish

def solve_quadratic(a, b, c):
    # a, b, c are the standard coefficients
    D = b**2 - 4*a*c
    if D < 0:
        return "No Real solution"
    
    # Ensure parentheses around (2*a) to avoid math errors
    x1 = (-b + math.sqrt(D)) / (2*a)
    x2 = (-b - math.sqrt(D)) / (2*a)
        
    if x1 == x2:
        return f"x = {round(x1, 10)}" # Clean up single-root cases
    return f"x = {round(x1, 10)}, {round(x2, 10)}"
