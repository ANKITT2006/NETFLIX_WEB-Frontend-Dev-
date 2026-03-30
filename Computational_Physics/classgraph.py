import matplotlib.pyplot as plt

x = 0
y = 1
h = 0.2
n = 5

x_values = []
y_values = []

for i in range(n):
    x_values.append(x)
    y_values.append(y)
    
    print(x, y)
    
    y = y + h * (x + y)
    x = x + h

# Add final point
x_values.append(x)
y_values.append(y)

print("final value", y)

# Plot graph
plt.plot(x_values, y_values, marker='o')
plt.xlabel("x values")
plt.ylabel("y values")
plt.title("Euler Method Graph")
plt.grid()

plt.show()