import numpy as np
import matplotlib.pyplot as plt

def deriv(f,a,method='central', h=0.01):
    if method== 'central' :
        return(f(a+h) -f(a-h))/(2*h)
    elif method=='forward':
        return (f(a+h)-f(a))/h
    elif method=='backward':
        return (f(a)-f(a-h))/h
    else:
        raise ValueError("Method false")
x=np.linspace(0,6,100)
y = lambda x: x*sin(x)
y(x)=f1
dydx= deriv(f1,x)
plt.plot(x,f1)


