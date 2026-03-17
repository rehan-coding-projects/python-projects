import math
import matplotlib.pyplot as plt

g = 9.8
m = 200
launch = float(input("Launch angle: "))
lrad = math.radians(launch)
v0 = float(input("Initial velocity: "))
y0 = 0.00001
dt = 0.001
t=0
  
x = 0
vx = v0 * math.cos(lrad)
y = 0.1
vy= v0 * math.sin(lrad)
xlist = [x]
ylist = [y]
k = 0.1

while y>0:
    ax = -k/m * vx
    ay = ((-k/m) * vy) - g
    vx += ax * dt
    vy += ay * dt
    x += vx * dt #Numerical integration methods
    y += vy * dt
    xlist.append(x)
    ylist.append(y)
    t += dt

plt.figure(figsize=(8,4))
plt.plot(xlist,ylist)
plt.title("Linear drag")
plt.xlabel("Horizontal distance (m)")
plt.ylabel("Vertical height(m)")
plt.grid(True)
plt.show()