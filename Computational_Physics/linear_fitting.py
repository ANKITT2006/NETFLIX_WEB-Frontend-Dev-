import matplotlib.pyplot as plt
x=[1,2,3,4]
y=[16,19,23,26]
sumx=0
sumy=0
sumxy=0
sumx2=0
n=len(x)
for i in range(n):
    sumx+=x[i]
    sumy+=y[i]
    sumxy+=x[i]*y[i]
    sumx2+=x[i]**2
b=(n*sumxy-sumx*sumy)/(n*sumx2-sumx**2)
a=(sumy-b*sumx)/n
print(sumx)
print(sumy)
print(sumxy)
print(sumx2)
print("a=",a)
print("b=",b)
plt.plot(x,y)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Linear Fitting")
plt.show()