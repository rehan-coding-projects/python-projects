#Method uses Cauchy's root bound theorem, a brute-force mechanism, and the Newton-Raphson method for finding roots of polynomials

import numpy as np
tol = 0.0000001
devtol = 1e-12
dx = 0.001
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
    for u in range(len(coeffs)):
        power = deg - u
        slope += power * coeffs[u] * x**(power - 1)
    return slope

def newtonraphson(xmid):
    x = xmid
    for k in range(1000):
        y = f(x)
        dy = df(x)
        if abs(dy)<devtol:
            return None
        xnew = x - (y/dy)
        if abs(xnew-x) < tol:
            return xnew
        x = xnew
    if k == 999:
        return None

for x in np.arange(-absbound,absbound,dx):
    if f(x) * f(x+dx) < 0:
        xmid = (x+(x+dx))/2
        root = newtonraphson(xmid)
        if root != None and abs(f(root))<tol and abs(root-xmid)<2:
            if len(sollist) == 0 or abs(root-sollist[-1])>tol:
                sollist.append(root)
        

for i in range(len(sollist)):
    root = sollist[i]
    print(f"x{i+1} = {round(root,4)}")
