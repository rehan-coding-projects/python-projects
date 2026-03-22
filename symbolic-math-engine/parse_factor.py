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

            if self.tokens[self.pos] != ")" or self.pos >= len(self.tokens):
                raise Exception("Expected )")
            self.pos += 1
            return node
        else:
            raise Exception("Invalid syntax")
        
