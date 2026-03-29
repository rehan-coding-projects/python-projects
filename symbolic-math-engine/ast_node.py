class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
    
    def __repr__(self):
        if self.left and self.right:
            return f"({self.left} {self.value} {self.right})"
        return str(self.value)

class NumNode:
    def __init__(self, value):
        self.value = value
    def evaluate(self):
        return self.value
    
class AddNode:
    def __init__(self, left, right):
        self.left = left
        self.right = right
    def evaluate(self):
        return self.left.evaluate() + self.right.evaluate()

class SubNode:
    def __init__(self, left, right):
        self.left = left
        self.right = right
    def evaluate(self):
        return self.left.evaluate() - self.right.evaluate()

class MultNode:
    def __init__(self, left, right):
        self.left = left
        self.right = right
    def evaluate(self):
        return self.left.evaluate() * self.right.evaluate()

class DivNode: 
    def __init__(self, left, right):
        self.left = left
        self.right = right
    def evaluate(self):
        return self.left.evaluate() / self.right.evaluate()

class ExpNode:
    def __init__(self, base, expo):
        self.base = base
        self.expo = expo
    def evaluate(self):
        return self.base.evaluate() ** self.expo.evaluate()
    
class UnaryMinusNode:
    def __init__(self, opr):
        self.opr = opr
    def evaluate(self):
        return -self.opr.evaluate()

    

#Node("*", Node("+", Node(3), Node(4)), Node(2))
