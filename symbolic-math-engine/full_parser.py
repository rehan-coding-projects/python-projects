from tokenizer import tokenizer
from ast_node import *



class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0
        self.in_function = False

    def parse_factor(self):
        
        if self.pos >= len(self.tokens):

            raise Exception("Unexpected end of input")
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
        elif current.isalpha() and isinstance(current, str):
            if self.pos + 1 < len(self.tokens) and self.tokens[self.pos + 1] == "(":
                return self.parse_function()
            
            self.pos +=1
            return VariableNode(current)
        else:
            raise Exception(f"Invalid syntax: {self.tokens}")      
    def parse_power(self):
        left = self.parse_factor()

        if self.pos < len(self.tokens) and self.tokens[self.pos] == "^":
            self.pos += 1
            right = self.parse_power()
            return ExpNode(left, right)

        return left 
    def parse_term(self):
        node = self.parse_power()
        print(f"[Term] pos={self.pos}, token={self.tokens[self.pos:]}")
        while self.pos < len(self.tokens):
            cur = self.tokens[self.pos]

            if cur in ("*", "/"):
                op = cur
                self.pos += 1
                right = self.parse_power()
                if op == "*":
                    node = MultNode(node, right)
                elif op == "/":
                    node = DivNode(node, right)
            elif cur =="(" or isinstance(cur, (int,float)) or isinstance(cur, str) and cur.isalpha() and not (self.pos + 1 < len(self.tokens) and self.tokens[self.pos+1] == "<"):
                right = self.parse_factor()
                node = MultNode(node, right)
            else:
                break
        return node
    def parse_expression(self):
        node = self.parse_term()

        while self.pos < len(self.tokens) and self.tokens[self.pos] not in (")",):
            op = self.tokens[self.pos]
            self.pos += 1
            right = self.parse_term()
            if op == "+":
                node = AddNode(node, right)
            elif op == "-":
                node = SubNode(node, right)
        return node
    def parse_function(self):
        name = self.tokens[self.pos]
        self.pos +=1

        if self.pos>= len(self.tokens) or self.tokens[self.pos] != "(":
            raise Exception("Expected (")
        self.pos+=1

        self.in_function = True
        arg = self.parse_expression()
        self.in_function = False
        if self.pos>= len(self.tokens) or self.tokens[self.pos] != ")":
            raise Exception("Expected )")
        
        self.pos+=1
        return FunctionNode(name, arg)

