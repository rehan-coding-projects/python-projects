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
    def evaluate(self, context={}):
        return self.value
    def __repr__(self):
        return str(self.value)
    
class AddNode:
    def __init__(self, left, right):
        self.left = left
        self.right = right
    def evaluate(self, context={}):
        left_val = self.left.evaluate(context)
        right_val = self.right.evaluate(context)

        if isinstance(left_val, (int,float)) and isinstance(right_val, (int, float)):
            return left_val + right_val
        
        return AddNode(left_val, right_val)
    
    def __repr__(self):
        return(f"({self.left} + {self.right})")

class SubNode:
    def __init__(self, left, right):
        self.left = left
        self.right = right
    def evaluate(self, context={}):
        left_val = self.left.evaluate(context)
        right_val = self.right.evaluate(context)

        if isinstance(left_val, (int,float)) and isinstance(right_val, (int, float)):
            return left_val - right_val
        
        return SubNode(left_val, right_val)
    def __repr__(self):
        return(f"({self.left} - {self.right})")

class MultNode:
    def __init__(self, left, right):
        print("Multiply:", left, right)
        self.left = left
        self.right = right
    def evaluate(self, context={}):
        left_val = self.left.evaluate(context)
        right_val = self.right.evaluate(context)

        if isinstance(left_val, (int,float)) and isinstance(right_val, (int, float)):
            return left_val * right_val
        
        return MultNode(left_val, right_val)
    def __repr__(self):
        return(f"({self.left} * {self.right})")

class DivNode: 
    def __init__(self, left, right):
        self.left = left
        self.right = right
    def evaluate(self, context={}):
        left_val = self.left.evaluate(context)
        right_val = self.right.evaluate(context)

        if isinstance(left_val, (int,float)) and isinstance(right_val, (int, float)):
            return left_val / right_val
        
        return DivNode(left_val, right_val)
    def __repr__(self):
        return(f"({self.left} / {self.right})")

class ExpNode:
    def __init__(self, base, expo):
        self.base = base
        self.expo = expo
    def evaluate(self, context={}):
        base_val = self.base.evaluate(context)
        expo_val = self.expo.evaluate(context)

        if isinstance(base_val, (int, float)) and isinstance(expo_val, (int, float)):
            return base_val ** expo_val
        return ExpNode(base_val, expo_val)
    
    def __repr__(self):
        return(f"({self.base} ^ {self.expo})")
    
class UnaryMinusNode:
    def __init__(self, opr):
        self.opr = opr
    def evaluate(self, context={}):
        val = self.opr.evaluate(context)

        if isinstance(val, (int, float)):
            return -val
        return UnaryMinusNode(val)
    
    def __repr__(self):
        return f"-({self.opr})"

class VariableNode: #Handles variables and symbolic operations
    def __init__(self, name):
        self.name = name
    
    def evaluate(self, context={}):
        if self.name in context:
            return context[self.name]
        return self
    
    def __repr__(self):
        return self.name

    

#Node("*", Node("+", Node(3), Node(4)), Node(2))
