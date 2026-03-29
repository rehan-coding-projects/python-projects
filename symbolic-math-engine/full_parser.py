from tokenizer import tokenizer
from ast_node import *



class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def parse_factor(self):
        current = self.tokens[self.pos]

        if isinstance(current, (int, float)):
            node = NumNode(current)
            self.pos += 1
            return node
        elif current == "-":
            self.pos+=1
            sepnode = self.parse_factor()
            
            return UnaryMinusNode(sepnode)
        elif current == "(":
            self.pos += 1

            node = self.parse_expression()

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
            return ExpNode(left, right)

        return left 
    def parse_term(self):
        node = self.parse_power()

        while self.pos < len(self.tokens) and self.tokens[self.pos] in ("*","/"):
            op = self.tokens[self.pos]
            self.pos += 1

            right = self.parse_power()
            if op == "*":
                node = MultNode(node, right)
            elif op == "/":
                node = DivNode(node, right)
        return node
    def parse_expression(self):
        node = self.parse_term()

        while self.pos < len(self.tokens) and self.tokens[self.pos] in ("+","-"):
            op = self.tokens[self.pos]
            self.pos += 1
            right = self.parse_term()
            if op == "+":
                node = AddNode(node, right)
            elif op == "-":
                node = SubNode(node, right)
        return node
