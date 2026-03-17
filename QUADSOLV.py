from math import sqrt

def solve_quadratic():
  print("ax^2 + bx + c")
  a = float(input("Enter a: "))
  b = float(input("Enter b: "))
  c = float(input("Enter c: "))

  if a == 0:
    print("Invalid quadratic")
    return

  D = b**2 - 4*a*c

  if D > 0:

    x1 = (-b + sqrt(D))/ (2*a)
    x2 = (-b - sqrt(D))/ (2*a)
    print("Two real roots: ")
    print("x1 = " + str(x1))
    print("x2 = "+ str(x2))

  elif D==0:
    x1 = (-b + sqrt(D))/ (2*a)
    print("One real root: ")
    print("x = " + str(x1))

  else:
    print("Imaginary roots, incapable of proccesing.")

solve_quadratic()
