import sympy as sp 

x,y = sp.symbols('x y')
f= x**2 +3*y**2-4*x*y
grad_x = sp.diff(f,x)
grad_y = sp.diff(f,y)
print('f(x,y)= ',f)
print("grad(f)= ",grad_x,grad_y) 