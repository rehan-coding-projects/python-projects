def tokenizer(expression):
    tokens = []
    current_number = ""

    for char in expression: 
        

        if char.isdigit() or char == ".":
            current_number += char

        elif char in "+-*/^()":
            if current_number != "":    
                tokens.append(float(current_number))
                current_number = ""
            tokens.append(char)
        
    if current_number != "":
        tokens.append(float(current_number))
    return tokens

def handle_parentheses(tokens):
    while "(" in tokens:
        open_index = None

        for i in range(len(tokens)):
            if tokens[i] == "(":
                open_index = i
            elif tokens[i] == ")":
                close_index = i

                sub_expr = tokens[open_index + 1:close_index]
                result = eval(sub_expr)

                tokens[open_index:close_index + 1] = [result]

                break
    return tokens


def handle_exp(tokens):
    i = len(tokens) - 1

    while i >= 0:
        if tokens[i] == "^":
            left = tokens[i-1]
            right = tokens[i+1]

            result = left ** right
            
            tokens[i-1:i+2] = [result]
            
            i = len(tokens) - 1 #Restart expression iteration
        else:
            i-=1
    return tokens    

def handle_mul_div(tokens):
    i = 0

    while i < len(tokens):
        if tokens[i] == "*" or tokens[i] == "/":
            left = tokens[i-1]
            right = tokens[i+1]

            if tokens[i] == "*":
                result = left * right
            elif tokens[i] == "/":
                result = left / right

            tokens[i-1:i+2] = [result]
            
            i = 0 #Restart expression iteration
        else:
            i+=1
    return tokens

def handle_add_sub(tokens):
    j = 0 #Counter

    while j < len(tokens):
        if tokens[j] == "+" or tokens[j] == "-":
            left = tokens[j-1]
            right = tokens[j+1]

            if tokens[j] == "+":
                result = left + right
            elif tokens[j] == "-":
                result = left - right
            
            tokens[j-1:j+2] = [result]

            j=0
        else:
            j+=1
    return tokens
    
def eval(tokens):
    tokens = handle_parentheses(tokens)
    tokens = handle_exp(tokens)
    tokens = handle_mul_div(tokens)
    tokens = handle_add_sub(tokens)
    return tokens[0]

expression = input("Enter expression: ")
tokens = tokenizer(expression)
result = eval(tokens)
print(result)
