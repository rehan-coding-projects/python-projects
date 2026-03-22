from math import sin, cos, tan, asin, acos, atan, radians, degrees, sqrt

def trig_main():
    print("\n📐 Trigonometry Toolbox (MAXED OUT)")
    print("1. sin, cos, tan of an angle (in degrees)")
    print("2. Convert degrees ↔ radians")
    print("3. Inverse trig: asin, acos, atan")
    print("4. Pythagorean Theorem")
    print("5. Area of triangle using sine (A = 1/2 ab sin C)")
    print("6. Solve triangle (SAS: two sides and included angle)")
    print("7. Solve triangle (AAS or ASA: two angles + one side)")
    print("8. Solve right triangle using SOH/CAH/TOA")
    print("q. Quit")

    choice = input("Enter your choice: ").lower()

    if choice == "1":
        angle_deg = float(input("Enter the angle in degrees: "))
        angle_rad = radians(angle_deg)
        print("sin(" + str(angle_deg) + ") =", sin(angle_rad))
        print("cos(" + str(angle_deg) + ") =", cos(angle_rad))
        print("tan(" + str(angle_deg) + ") =", tan(angle_rad))

    elif choice == "2":
        print("1. Convert degrees to radians")
        print("2. Convert radians to degrees")
        sub = input("Enter your choice: ")
        if sub == "1":
            angle_deg = float(input("Enter the angle in degrees: "))
            angle_rad = radians(angle_deg)
            print(str(angle_deg) + " degrees = " + str(angle_rad) + " radians")
        elif sub == "2":
            angle_rad = float(input("Enter the angle in radians: "))
            angle_deg = degrees(angle_rad)
            print(str(angle_rad) + " radians = " + str(angle_deg))
        else:
            print("Invalid choice")
# use an approximation for pi
    elif choice == "3":
        print("Inverse trig functions:")
        print("1. asin (for sin⁻¹)")
        print("2. acos (for cos⁻¹)")
        print("3. atan (for tan⁻¹)")
        sub = input("Choose 1–3: ")
        val = float(input("Enter value (-1 to 1 for sin/cos, any real for tan): "))
        if sub == "1":
            print("asin =", degrees(asin(val)))
        elif sub == "2":
            print("acos =", degrees(acos(val)))
        elif sub == "3":
            print("atan =", degrees(atan(val)))
        else:
            print("Invalid choice.")

    elif choice == "4":
        a = float(input("Enter the length of side a: "))
        b = float(input("Enter the length of side b: "))
        c = sqrt(a**2 + b**2)
        print("The length of the hypotenuse (c) is:", c)

    elif choice == "5":
        a = float(input("Enter the length of side a: "))
        b = float(input("Enter the length of side b: "))
        angle_deg = float(input("Enter the angle in degrees: "))
        angle_rad = radians(angle_deg)
        area = 0.5 * a * b * sin(angle_rad)
        print("The area of the triangle is:", area)

    elif choice == "6":
        a = float(input("Enter side a: "))
        b = float(input("Enter side b: "))
        C_deg = float(input("Enter included angle C (degrees): "))
        C_rad = radians(C_deg)
        c = sqrt(a**2 + b**2 - 2*a*b*cos(C_rad))  # Law of Cosines
        print("Third side c =", c)

    elif choice == "7":
        A = float(input("Enter angle A (degrees): "))
        B = float(input("Enter angle B (degrees): "))
        C = 180 - A - B
        print("Angle C =", C)
        known = input("Which side do you know (a, b, or c)? ").lower()
        side = float(input("Enter side " + known + ": "))
        if known == "a":
            b = side * sin(radians(B)) / sin(radians(A))
            c = side * sin(radians(C)) / sin(radians(A))
            print("b =", round(b, 3))
            print("c =", round(c, 3))
        elif known == "b":
            a = side * sin(radians(A)) / sin(radians(B))
            c = side * sin(radians(C)) / sin(radians(B))
            print("a =", round(a, 3))
            print("c =", round(c, 3))
        elif known == "c":
            a = side * sin(radians(A)) / sin(radians(C))
            b = side * sin(radians(B)) / sin(radians(C))
            print("a =", round(a, 3))
            print("b =", round(b, 3))
        else:
            print("Invalid side.")

    elif choice == "8":
        print("Solve right triangle using SOH/CAH/TOA")
        angle_deg = float(input("Enter non-right angle (degrees): "))
        known = input("Which side do you know? (opp/adj/hyp): ").lower()
        val = float(input("Enter length of " + known + ": "))
        angle_rad = radians(angle_deg)
        if known == "opp":
            adj = val / tan(angle_rad)
            hyp = val / sin(angle_rad)
            print("adj =", adj)
            print("hyp =", hyp)
        elif known == "adj":
            opp = val * tan(angle_rad)
            hyp = val / cos(angle_rad)
            print("opp =", opp)
            print("hyp =", hyp)
        elif known == "hyp":
            opp = val * sin(angle_rad)
            adj = val * cos(angle_rad)
            print("opp =", opp)
            print("adj =", adj)
        else:
            print("Invalid input.")

trig_main()
