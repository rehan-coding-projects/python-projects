from tokenizer import tokenizer
from full_parser import Parser
import math


def evaluate(expr, context=None):
    if context is None:
        context={}
    
    tokens = tokenizer(expr)
    parser = Parser(tokens)
    ast = parser.parse_expression()

    result = ast.evaluate(context)
    return result

[]
