 #gradient
import sympy as sp
x,y,z=sp.symbols('x y z')
f=(2*x**2+3*y**3+4*z**3)
grad=[sp.diff(f,x)+sp.diff(f,y)+sp.diff(f,z)] 
print("gradient:", grad)


#divergence
import sympy as sp

x, y, z = sp.symbols('x y z')

F1 = x**2 * y
F2 = y**2 * z
F3 = z**2 * x

div =[ sp.diff(F1, x) + sp.diff(F2, y) + sp.diff(F3, z)]

print("Divergence:", div)


#curl
import sympy as sp

x, y, z = sp.symbols('x y z')

F1 = x**2 * y
F2 = y**2 * z
F3 = z**2 * x

curl_x = sp.diff(F3, y) - sp.diff(F2, z)
curl_y = sp.diff(F1, z) - sp.diff(F3, x)
curl_z = sp.diff(F2, x) - sp.diff(F1, y)

curl = [curl_x, curl_y, curl_z]

print("Curl:", curl)

