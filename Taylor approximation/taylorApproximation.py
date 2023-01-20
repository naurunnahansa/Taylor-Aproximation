from sympy import *
from sympy.plotting import plot

def taylorAprox(f,a,deg):
    derivs = [f]
    output = [f.subs(x,a)]
    eq = output[0]
    for i in range(1,deg):
        derivs.append(diff(derivs[i-1]))
        output.append(derivs[i].subs(x,a)*(x-a)**i/factorial(i))
        eq += output[i]
    return eq

def plotEq(eq01, eq02):
    p1 = plot(eq01, show=False)
    p2 = plot(eq02, show=False)
    p1.append(p2[0])
    p1.show()     


x = symbols('x')
f = cos(x)
df = taylorAprox(f,3.141/4,5)
plotEq(f,df)