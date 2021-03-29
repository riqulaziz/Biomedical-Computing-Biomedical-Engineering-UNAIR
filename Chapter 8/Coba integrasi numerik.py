import math as mt
def f(x):
    return x**(2)*mt.cos(x**(2))
xi=[]
x0=1.5
x1=2.5
h=0.1
n=(x1-x0)/h
fa=f(x0)
fn=f(x1)

while x0<x1+h:
    xi.append(x0)
    x0=x0+h

print("x=",xi)
length=len(xi)

fxi=[]
for i in range(0,length):
    fx=f(xi[i])
    fxi.append(fx)
print("Nilai hasil fungsi =",fxi)

sigma=0
for i in range(1,length-1):
    sigma=sigma+fxi[i]
print("sigma =",sigma)
## METODE TRAPEZOID
hasil=(fa+2*sigma+fn)*h/2
print("Hasil Trapezoid =", hasil)

sigmaGanjil=0
sigmaGenap=0
#METODE SIMPSON
for i in range(1,length-1):
    if i%2!=0 :
        sigmaGanjil=sigmaGanjil+fxi[i]
    else:
        sigmaGenap=sigmaGenap+fxi[i]
print("hasil sigma ganjil = ",sigmaGanjil,", hasil sigma genap =",sigmaGenap)
simpson=(fa+4*sigmaGanjil+2*sigmaGenap+fn)*h/3
print("Nilai Hasil Simpson =",simpson)

from sympy import *
x=Symbol('x')
fd=x**(2)*cos(x**(2))
integral=fd.integrate(x)
print("Hasil Integral=",integral)

from scipy import integrate
hasilIntegral=integrate.quad(f,1.5,2.5)
print("Hasil Integral Eksak",hasilIntegral)

er_simson=abs(simpson-hasilIntegral[0])
er_trape=abs(hasil-hasilIntegral[0])
print("Hasil Eror Sympson = ", er_simson)
print("Hasil Eror Trapezoid = ", er_trape)


