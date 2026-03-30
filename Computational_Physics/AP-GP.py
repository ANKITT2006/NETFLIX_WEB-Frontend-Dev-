#AP
import math
A=[2,5,8,11,14]
a=A[0]
d=(A[1]-A[0])
n=10
last_term=A[-1]
t=a+(n-1)*d
print(t)
s=n*(2*a+(n-1)*d)/2
print(s)
for i in range(9):
    next_term=last_term + d
    A.append(next_term)
    last_term=next_term
print(A)



#GP
G=[3,6,12,24,48]
a=G[0]
r=G[1]/G[0]
n=10
last_term=G[-1]
t=a*(r**(n-1))
print(t)
if r>1:
    s=a*(r**n-1)//(r-1)
else:
    s=a*(1-r**n)//(1-r)
print(s)
for i in range(9):
    next_term=last_term*r
    G.append(next_term)
    last_term=next_term
print(G)    


