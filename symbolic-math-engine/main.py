from tokenizer import tokenizer
from full_parser import Parser
import math
from astsolver import *
from engine import evaluate
from eqsolver import *

def process(expr, context=None):
    if context is None:
        context = {
            'x':0,
            'y':0,
            'pi' : math.pi,
            'e' : math.e
        }

    if "=" in expr:
        left_str, right_str = expr.split("=")

        _, left_ast = evaluate(left_str, context)
        _, right_ast = evaluate(right_str, context)

        print(f"DEBUG AST STRUCTURE: {left_ast}")
        ast = SubNode(left_ast, right_ast)
    
        a,b,c = extract_quadratic(ast)
        
        if a != 0:
            return solve_quadratic(a,b,c)
        else:

            return solve_linear(b,c)
        
    value, ast = evaluate(expr, context)
    return value

