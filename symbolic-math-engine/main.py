from tokenizer import tokenizer
from full_parser import Parser


expr = input("Enter expression : ")

tokens = tokenizer(expr)
parser = Parser(tokens)
ast = parser.parse_expression()
result = ast.evaluate({"x": 4})
print(tokens)
print(result)

