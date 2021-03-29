import math as mt
import matplotlib.pyplot as plt
from sympy import *
def f(x):
    return x*mt.sin(x)
x0=1
h=0.0001
fow=(f(x0+h)-f(x0))/h
back=(f(x0)-f(x0-h))/h
cent=(f(x0+h)-f(x0-h))/2*h
print(fow)
plt.plot(x0,f(x0))
##### Untuk Mengatahui Persamaan Hasil Turunan#########
x=Symbol("x")
fd=x*sin(x)
dydx=fd.diff(x)
print("turunan pertama =",dydx)
####### Mengetahui Hasil Sebenarnya dari Perhitungan Turunan Kontinu ########
fx=lambdify(x,dydx)
print("f'(1) =",fx(1))
er=abs(fx(1)-fow)
print("Nilai Eror dari hasil perhitungan =", er)
