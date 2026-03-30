import matplotlib.pyplot as plt
import math
k=1
x=[i for i in range(-10,11)]
U=[0.5*k*math.pow(i,2) for i in x]
print(U)
plt.plot(x,U)
plt.xlabel("Displacement")
plt.ylabel("Potential Energy")
plt.title("Potential Energy vs Displacement of Spring-Mass System")
plt.show()

