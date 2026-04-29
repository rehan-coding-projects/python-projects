from main import evaluate
import math

def solve_linear(expr):
    left, right = expr.split("=")

    def f(x):
        context ={
            "x" : x,
            "pi":math.pi,
            "e":math.e
        }
        return evaluate(left,context) - evaluate(right, context)
    
    b = f(0)
    a = f(1) - b

    if a =="0":
        return "No unique solution"
    
    return -b/a
