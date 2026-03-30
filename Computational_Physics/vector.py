#using libraries

import numpy as np
import math

a=np.array([1,2,3])
b=np.array([1,1,0])
c=np.array([1,2,-3])

mag_a=np.linalg.norm(a)
mag_b=np.linalg.norm(b)
mag_c=np.linalg.norm(c)
print("Magnitude of a is ",mag_a)
print("Magnitude of b is ",mag_b)
print("Magnitude of c is ",mag_c)

unitvector_a=a/mag_a
print("Unit vector of a is ",unitvector_a)

res_a_and_c=(a+c)
print("Resultant vector of a and c is ",res_a_and_c)

dot_ab=np.dot(a,b)
print("Dot product of a and b is ",dot_ab)
angle_ab=math.acos(dot_ab/(mag_a*mag_b))
print("Angle between a and b is ",math.degrees(angle_ab))

result=a*np.cross(b,c)
print("Result of a cross b cross c is ",result)