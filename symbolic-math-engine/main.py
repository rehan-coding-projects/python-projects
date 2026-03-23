from tokenizer import tokenizer
from full_parser import Parser

def main():
    expr = input("Enter expression : ")

    tokens = tokenizer(expr)
    parser = Parser(tokens)

    ast = parser.parse_expression()

    print(ast)

main()