from tokenizer import tokenizer
from full_parser import Parser

def evaluate(expr, context=None):
    if context is None:
        context={}

    tokens = tokenizer(expr)
    parser = Parser(tokens)
    ast = parser.parse_expression()
    
   
    return ast.evaluate(context), ast