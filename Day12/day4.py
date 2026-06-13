import sympy as sp

x = sp.symbols('x')
f = x**2
definite_integral = sp.integrate(f,(x,0,2))
indefinite_integral = sp.integrate(f)
print("the definite integral")
print(definite_integral)
print("the indefinite integral")
print(indefinite_integral)