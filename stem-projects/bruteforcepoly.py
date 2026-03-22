import numpy as np
tol = 0.00001
dx = 0.001
sollist = []
deg = int(input("Enter degree: "))
coeffs = []
for z in range(deg, -1, -1):
    coef = float(input(f"Enter coefficient for x^{z}: "))
    coeffs.append(coef)

def polynomial(x):
    result = 0
    for i in range(len(coeffs)):
        power = deg - i
        result += coeffs[i] * (x**power)
    return result

for x in np.arange(-100,100,0.001):
    xs = polynomial(x)
    if abs(xs) < tol:
        if len(sollist) == 0 or abs(x-sollist[-1])>tol:
            sollist.append(x)

    

for i in range(len(sollist)):
    root = sollist[i]
    print(f"x{i+1} = {round(root,4)}")
