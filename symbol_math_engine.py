list1 = []
string = input("Enter expression: ")
num = ""
print(type(string))
for i in range(len(string)):
    char = string[i]
    if char.isdigit() or char == ".":
        num = num + char
    elif char in "+-*/":
        if num != "":    
            list1.append(float(num))
            num = ""
        list1.append(char)
    print("num building: ", num)
    
if num != "":
    list1.append(float(num))

if "*" in list1:
    g = list1.index("*")
    product = float(list1[g-1]) * float(list1[g+1])
    del list1[g-1:g+2]
    list1.insert(g-1, product)

print(list1)
