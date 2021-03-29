import math as mt
import matplotlib.pyplot as mtp
def Rungkuta(x,w):
    return (-2*(x**3))+(12*(x**2))-(20*x)+8.5
### Exact Value###
import sympy
sympy.init_printing()
y=sympy.Function('y')
x=sympy.symbols('x')
ode=sympy.Eq(y(x).diff(x),((-2*(x**3))+(12*(x**2))-(20*x)+8.5))
generalSolution=sympy.dsolve(ode,y(x))
value=generalSolution.subs([(x,0),(y(0),1)])
odeSolution=generalSolution.subs([(value.rhs,value.lhs)])
print(odeSolution)
###
odeExpression=odeSolution.rhs
print('Exact Solution =',odeExpression)
from sympy.utilities.lambdify import lambdify
odeFunction=lambdify((x,),odeExpression,modules='numpy')
#####
a=0 # batas bawah
ai=a
b=4 #batas atas
h=eval(input('Masukkan jumlah h ='))
#h=(b-a)/N
x=0
w=1
xi=[]
wi=[]
yi=[]
##
while a<b:
    w1=h*Rungkuta(x,w)
    w2=h*Rungkuta(x+0.5*h,w+0.5*w1*h)
    w3=h*Rungkuta(x+0.5*h,w+0.5*h*w2)
    w4=h*Rungkuta(x+h,w+w3*h)
    w=w+(w1+2*w2+2*w3+w4)/6
    a=a+h
    x=a
    y=odeFunction(x)
    eror=abs(y-w)
    xi.append(x)
    wi.append(w)
    yi.append(y)
    print('nilai t =',x,'nilai w =',w,'nilai y =',y, 'eror =',eror)
mtp.plot(xi,wi,'g*',xi,yi,'r')
mtp.xlabel('t (sekon)')
mtp.ylabel(" y' ")
mtp.title('Grafik Metode Euler')
mtp.show()