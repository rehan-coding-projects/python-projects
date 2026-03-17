from math import sqrt

def solve_linear():
  a = float(input("Enter the value of a: "))
  b = float(input("Enter the value of b: "))
  c = float(input("Enter the value of c: "))

  if a == 0:
    if b == c:
      print("Infinite solutions")
    else:
      print("No solutions")
  else:
    x = (c - b) / a
    print("The solution is x = ", {x})

def expand_binomial():
  print("Expanding (x + a)(x + b)")
  a = float(input("Enter the value of a: "))
  b = float(input("Enter the value of b: "))

  term1 = 1
  term2 = a + b
  term3 = a * b
  print("Expanded form: x^2 + ", term2, "x + ", term3)

def factor_quadratic():
  print("Factoring x^2 + bx + c = 0")
  b = int(input("Enter b: "))
  c = int(input("Enter c: "))
  found = False
  for i in range(-100, 101):
      for j in range(-100, 101):
            if i + j == b and i * j == c:
                print("Factored form: (x +", i, ")(x +", j, ")")
                found = True
                break
      if found:
          break
  if not found:
      print("Could not factor. Try quadratic formula.")

def evaluate_expression():
    print("\nEvaluating expression ax + b")
    a = float(input("Enter a: "))
    b = float(input("Enter b: "))
    x = float(input("Enter value of x: "))
    result = a * x + b
    print("Result:", result)

def solve_system():
    print("\nSolving:")
    print("eq1: a1x + b1y = c1")
    print("eq2: a2x + b2y = c2")
    a1 = float(input("a1: "))
    b1 = float(input("b1: "))
    c1 = float(input("c1: "))
    a2 = float(input("a2: "))
    b2 = float(input("b2: "))
    c2 = float(input("c2: "))
    D = a1 * b2 - a2 * b1
    Dx = c1 * b2 - c2 * b1
    Dy = a1 * c2 - a2 * c1
    if D == 0:
        if Dx == 0 and Dy == 0:
            print("Infinite solutions")
        else:
            print("No solution")
    else:
        x = Dx / D
        y = Dy / D
        print("x =", x)
        print("y =", y)

def solve_quadratic():
    print("\nSolving ax^2 + bx + c = 0")
    a = float(input("Enter a: "))
    b = float(input("Enter b: "))
    c = float(input("Enter c: "))
    if a == 0:
        print("Not a quadratic. Try linear solver.")
        return
    D = b**2 - 4 * a * c
    if D < 0:
        print("No real roots")
    elif D == 0:
        x = -b / (2 * a)
        print("One real root: x =", x)
    else:
        x1 = (-b + sqrt(D)) / (2 * a)
        x2 = (-b - sqrt(D)) / (2 * a)
        print("Two real roots: x1 =", x1, "x2 =", x2)

def algetool():
    print("\n📦 Algebra Toolbox")
    print("1. Solve linear equation (ax + b = c)")
    print("2. Expand binomial (x + a)(x + b)")
    print("3. Factor quadratic (x^2 + bx + c)")
    print("4. Evaluate expression (ax + b at x = ?)")
    print("5. Solve system of 2 equations")
    print("6. Solve quadratic (ax^2 + bx + c = 0)")

    choice = input("Enter your choice: ").lower()

    if choice == "1":
        solve_linear()
    elif choice == "2":
        expand_binomial()
    elif choice == "3":
        factor_quadratic()
    elif choice == "4":
        evaluate_expression()
    elif choice == "5":
        solve_system()
    elif choice == "6":
        solve_quadratic()
    else:
        print("Invalid option.")

    print("Exiting Algebra Toolbox.")

algetool()
