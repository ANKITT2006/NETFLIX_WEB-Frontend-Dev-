x = 0
y = 1
h = 0.2
n = 5
for i in range(n):
     y = y + h * (x + y)
     x = x + h

print("Final value:", y)