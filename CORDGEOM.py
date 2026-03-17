from math import sqrt


def distance(x1, y1, x2, y2):
    """Distance between two points."""
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def midpoint(x1, y1, x2, y2):
    """Midpoint of two points."""
    return ((x1 + x2) / 2, (y1 + y2) / 2)
def slope(x1, y1, x2, y2):
    """Slope of two points."""
    if x2 - x1 == 0:
        return None
    return (y2 - y1) / (x2 - x1)


def main():
  print("Coordinate Geometry toolbox:")
  print("1. Distance between two points")
  print("2. Midpoint of two points")
  print("3. Slope of two points")
  choice = input("Enter your choice (1-3): ")

  if choice == "1":
    print("Distance calculator: ")
    x1 = float(input("Enter the x-coordinate of the first point: "))
    y1 = float(input("Enter the y-coordinate of the first point: "))
    x2 = float(input("Enter the x-coordinate of the second point: "))
    y2 = float(input("Enter the y-coordinate of the second point: "))
    d = distance(x1, y1, x2, y2)
    print("The distance between the two points is:", d)

  elif choice == "2":
      print("Midpoint calculator: ")
      x1 = float(input("Enter the x-coordinate of the first point: "))
      y1 = float(input("Enter the y-coordinate of the first point: "))
      x2 = float(input("Enter the x-coordinate of the second point: "))
      y2 = float(input("Enter the y-coordinate of the second point: "))
      m = midpoint(x1, y1, x2, y2)
      print("The midpoint between two points is:", m)

  elif choice == "3":
      print("Slope calculator: ")
      x1 = float(input("Enter the x-coordinate of the first point: "))
      y1 = float(input("Enter the y-coordinate of the first point: "))
      x2 = float(input("Enter the x-coordinate of the second point: "))
      y2 = float(input("Enter the y-coordinate of the second point: "))
      s = slope(x1, y1, x2, y2)
      if s == None:
        print("The slope of the two points is undefined.")
      else:
        print("The slope of the two points is:", s)


main()
