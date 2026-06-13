import sympy as sp 
x,y= sp.symbols('x y')
f = x**2 + y**2
grad_x =sp.diff(f,x)
grad_y =sp.diff(f,y)
print('f(x,y)= ',f)
print("grad(f)= ",grad_x,grad_y)