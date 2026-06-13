import sympy as sp 


x = sp.symbols('x')
f = sp.exp(-x)
indefinite_integral = sp.integrate(f,x)
print("Indefinite integral of f(x):",indefinite_integral)
definiteintegral = sp.integrate(f,(x,0,sp.oo))
print("Definite integral of f(x) from 0 to infinity:",definiteintegral)