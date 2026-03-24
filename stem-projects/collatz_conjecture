import matplotlib.pyplot as plt

x=0
xlist = []
ylist = []
num = int(input("Enter an integer: "))
orignum = num
ylist.append(num) #Starting number
xlist.append(x) #Base count

while num != 1:
    if num % 2 == 0:
        num = num / 2
        x += 1
        ylist.append(num)
        xlist.append(x)
        
    elif num % 2 == 1:
        num = 3*num + 1
        x += 1
        ylist.append(num)
        xlist.append(x)


plt.plot(xlist, ylist) #Plotting on the matplotlib grid

plt.xlabel("Operation count")
plt.ylabel("Resultant calculation")
plt.title(f"Collatz conjecture calculations for {orignum}")

print(f''' 
Highest number reached = {max(ylist)}
Total count required to hit 0 for original number = {xlist[-1]}
''')
plt.show()
