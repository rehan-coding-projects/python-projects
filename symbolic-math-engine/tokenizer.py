def tokenizer(expr):
    tokens = []
    i = 0
    while i<len(expr):
        char = expr[i]

        if char.isdigit() or char == ".":
            num = char
            dot_count = 1 if char =="." else 0
            i+=1

            while i < len(expr) and (expr[i].isdigit() or expr[i] == "."):
                if expr[i] == ".":
                    dot_count +=1
                    if dot_count > 1:
                        raise Exception("Expected 1 decimal only")
                num += expr[i]
                i+=1
            tokens.append(int(num))
        
        elif char.isalpha():
            tokens.append(char)
            i+=1
        
        elif char in "+-*/^()":
            tokens.append(char)
            i+=1
        
        elif char == " ":
            i+=1

        else: 
            raise Exception("Invalid syntax")
        
    return tokens

