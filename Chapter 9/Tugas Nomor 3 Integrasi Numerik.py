import math as mt
def poly(r,N=20,b=1):
    return (mt.exp(-3*r**2/(2*N*b**2))*4*mt.pi*r**2)*((3/(2*mt.pi*N*b**2))**(3/2))
ti=[]
t0=0 # Waktu Awal
t1=1 # Waktu Akhir
n=10
h=(t1-t0)/n
fa=poly(t0)
fn=poly(t1)
## pengisian matriks
while t0<t1+h:
    ti.append(t0)
    t0=t0+h
print('nilai t=',ti)
panjang=len(ti)
####
velo=[]
for i in range (0, panjang):
    v=poly(ti[i])
    velo.append(v)
print('Nilai hasil fungsi =',velo)
###
length=len(velo)
sigma=0
for i in range(1,length-1):
    sigma=sigma+velo[i]
print("sigma =",sigma)
## METODE TRAPEZOID
hasil=(fa+2*sigma+fn)*h/2
print("Hasil Trapezoid =", hasil)
####
sigmaGanjil=0
sigmaGenap=0
#METODE SIMPSON
for i in range(1,length-1):
    if i%2!=0 :
        sigmaGanjil=sigmaGanjil+velo[i]
    else:
        sigmaGenap=sigmaGenap+velo[i]
print("hasil sigma ganjil = ",sigmaGanjil,", hasil sigma genap =",sigmaGenap)
simpson=(fa+4*sigmaGanjil+2*sigmaGenap+fn)*h/3
print("Nilai Hasil Simpson =",simpson)

from sympy import *
r=Symbol('r')
N=20
b=1
fd=(exp(-3*r**2/(2*N*b**2))*4*pi*r**2)*((3/(2*pi*N*b**2))**(3/2))
integral=fd.integrate(r)
print("Hasil Integral=",integral)

from scipy import integrate
hasilIntegral=integrate.quad(poly,0,1)
print("Hasil Integral Eksak",hasilIntegral)

er_simson=abs(simpson-hasilIntegral[0])
er_trape=abs(hasil-hasilIntegral[0])
print("Hasil Eror Sympson = ", er_simson)
print("Hasil Eror Trapezoid = ", er_trape)


