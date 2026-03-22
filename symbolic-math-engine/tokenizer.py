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