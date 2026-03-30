#using loops

import numpy as np
import math

a=np.array([1,2,3])
b=np.array([1,1,0])
c=np.array([1,2,-3])
n=len(a)
mag_a=math.sqrt(sum(a[i]**2 for i in range(n)))
mag_b=math.sqrt(sum(b[i]**2 for i in range(n)))
mag_c=math.sqrt(sum(c[i]**2 for i in range(n)))

unitvector_a=a/mag_a
print("unit vector of a is ",unitvector_a)

resultantvector_ac=a+c
print("resultantvector_ac is ",resultantvector_ac)

dot_ab=np.dot(a,b)

angle_ab=math.acos(dot_ab/(mag_a*mag_b))
print("Angle between a and b is ",math.degrees(angle_ab))

cross_abc=a*np.cross(b,c)
print("Result of a cross b cross c is ",cross_abc)