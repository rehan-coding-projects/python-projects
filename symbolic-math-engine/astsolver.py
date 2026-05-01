from ast_node import *

def extract_quadratic(node):
    a, b, c = 0, 0, 0

    def get_value(n):
        """Helper to get value even if it's wrapped in a UnaryMinusNode."""
        if hasattr(n, 'value'):
            return n.value
        if type(n).__name__ == "UnaryMinusNode" and hasattr(n.opr, 'value'):
            return -n.opr.value
        return None

    def visit(n, sign=1):
        nonlocal a, b, c
        if n is None: return
        
        node_type = type(n).__name__

        if node_type == "AddNode":
            visit(n.left, sign); visit(n.right, sign)
        elif node_type == "SubNode":
            visit(n.left, sign); visit(n.right, -sign)
        elif node_type == "UnaryMinusNode":
            visit(n.opr, -sign)
        elif node_type == "NumNode":
            c += sign * n.value
        elif node_type == "VariableNode":
            if str(n.name).strip() == "x":
                b += sign * 1
        elif node_type == "ExpNode":
            base = n.base.name if hasattr(n.base, 'name') else n.base
            expo = n.expo.value if hasattr(n.expo, 'value') else n.expo
            if str(base).strip() == "x" and int(float(expo)) == 2:
                a += sign * 1
                return # Stop the leak!
        elif node_type == "MultNode":
            val_l = get_value(n.left)
            val_r = get_value(n.right)

            if val_l is not None:
                coeff, target = val_l * sign, n.right
            elif val_r is not None:
                coeff, target = val_r * sign, n.left
            else:
                visit(n.left, sign); visit(n.right, sign)
                return

            t_type = type(target).__name__
            if t_type == "VariableNode" and str(target.name).strip() == "x":
                b += coeff
                return 
            elif t_type == "ExpNode":
                t_base = target.base.name if hasattr(target.base, 'name') else target.base
                t_expo = target.expo.value if hasattr(target.expo, 'value') else target.expo
                if str(t_base).strip() == "x" and int(float(t_expo)) == 2:
                    a += coeff
                    return 
            visit(target, 1 if coeff > 0 else -1)

    visit(node)
    print(f"DEBUG FINAL: a={a}, b={b}, c={c}")
    return a, b, c
def is_quadratic(node):
    try:
        a,b,c = extract_quadratic(node)
        return a!=0
    except:
        return False 


def extract_linear(node):
    
    a = 0
    b = 0

    def visit(n, sign=1):
        nonlocal a, b
        
        if isinstance(n, AddNode):
            visit(n.left, sign)
            visit(n.right, sign)

        elif isinstance(n, SubNode):
            visit(n.left, sign)
            visit(n.right, -sign)

        elif isinstance(n, NumNode):
            b += sign * n.value

        elif isinstance(n, VariableNode):
            if n.name == "x":
               a += sign 
            elif n.name in ("pi", "e"):
                val = n.evaluate({"pi" : math.pi, "e" : math.e})
                b += sign*val
            else:
                raise Exception(f"Unknown variable: {n.name}")
        elif isinstance(n, UnaryMinusNode):
            visit(n.opr, -sign)
            
        elif isinstance(n, MultNode):
            if isinstance(n.right, NumNode) and isinstance(n.left, VariableNode):
                a += sign * n.right.value
            elif isinstance(n.left, NumNode) and isinstance(n.right, VariableNode):
                a+=sign * n.left.value
            else:
                raise Exception("Unsupported multiplication")

        else:
            raise Exception("Unsupported expression")

    visit(node)
        
    return a, b
