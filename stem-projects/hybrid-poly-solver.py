#Method uses Cauchy's root bound theorem, a brute-force mechanism, and the Newton-Raphson method for finding roots of polynomials

import numpy as np
tol = 1e-6
devtol = 1e-6
dx = 0.0005
roottol = 5e-2
sollist = []
deg = int(input("Enter degree: "))
coeffs = []
for z in range(deg, -1, -1):
    coef = float(input(f"Enter coefficient for x^{z}: "))
    coeffs.append(coef)

def cauchy():
    ledcoeff = abs(coeffs[0])
    div = []
    for d in range(1, len(coeffs)):
        jkl = abs(coeffs[d])/ledcoeff
        div.append(jkl)
    bound = 1+max(div)
    return bound    
absbound = cauchy()    

def f(x):
    result = 0
    for i in range(len(coeffs)):
        power = deg - i
        result += coeffs[i] * (x**power)
    return result
    
def df(x):
    slope = 0
    for u in range(len(coeffs) - 1):
        power = deg - u
        slope += power * coeffs[u] * x**(power - 1)
    return slope

def newtonraphson(xmid):
    x = xmid
    for k in range(3000):
        y = f(x)
        dy = df(x)
        if abs(dy)<devtol:
            dy=devtol         #Handles near-zero derivatives(likely case of repeated roots)
        xnew = x - (y/dy)
        if abs(xnew-x) < tol:
            return xnew
        x = xnew
    if k == 999:
        return None
    return x

for x in np.arange(-absbound,absbound,dx):
    root = None

    if f(x) * f(x+dx) < 0: 
        xmid = (x+(x+dx))/2
        root = newtonraphson(xmid)
    elif abs(f(x)) < tol and abs(df(x)) < devtol:
        root = newtonraphson(x)
        

    if root is not None and abs(f(root))<tol:
        root = round(root, 2)
        if all(abs(root-sollist[-1])>roottol for r in sollist):
            sollist.append(root)
        

for i in range(len(sollist)):
    root = sollist[i]
    print(f"x{i+1} = {round(root,4)}")
