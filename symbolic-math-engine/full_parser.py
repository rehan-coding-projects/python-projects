from tokenizer import tokenizer
from ast_node import Node


class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def parse_factor(self):
        current = self.tokens[self.pos]

        if isinstance(current, (int, float)):
            node = Node(current)
            self.pos += 1
            return node
        elif current == "(":
            self.pos += 1

            node = self.parse_factor()

            if self.pos >= len(self.tokens) or self.tokens[self.pos] != ")":
                raise Exception("Expected )")
            self.pos += 1
            return node
        else:
            raise Exception("Invalid syntax")      
    def parse_power(self):
        left = self.parse_factor()

        if self.pos < len(self.tokens) and self.tokens[self.pos] == "^":
            self.pos += 1
            right = self.parse_power()
            return Node("^", left, right)

        return left 
    def parse_term(self):
        node = self.parse_power()

        while self.pos < len(self.tokens) and self.tokens[self.pos] in ("*","/"):
            op = self.tokens[self.pos]
            self.pos += 1

            right = self.parse_power()
            node = Node(op, node, right)
        return node
    def parse_expression(self):
        node = self.parse_term()

        while self.pos < len(self.tokens) and self.tokens[self.pos] in ("+","-"):
            op = self.token[self.pos]
            self.pos += 1
            right = self.parse_term()
            node = Node(op, node, right)
        return node
