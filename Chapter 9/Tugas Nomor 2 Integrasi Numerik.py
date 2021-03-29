import math as mt
def poisel(z,L=91.44,u=0.01,d=0.1,p=1,g=9.81,R=10):
    a=64*L*u/(p*d**2)
    return (8*R**2)/(d**2)*(-a+mt.sqrt(a**2+8*g*(z+L)))
ti=[]
t0=5 # Waktu Awal
t1=50 # Waktu Akhir
n=5000
h=(t1-t0)/n
fa=poisel(t0)
fn=poisel(t1)
## pengisian matriks
while t0<t1+h:
    ti.append(t0)
    t0=t0+h
print('nilai t=',ti)
panjang=len(ti)
####
pois=[]
for i in range (0, panjang):
    v=poisel(ti[i])
    pois.append(v)
print('Nilai hasil fungsi =',pois)
###
length=len(pois)
sigma=0
for i in range(1,length-1):
    sigma=sigma+pois[i]
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
        sigmaGanjil=sigmaGanjil+pois[i]
    else:
        sigmaGenap=sigmaGenap+pois[i]
print("hasil sigma ganjil = ",sigmaGanjil,", hasil sigma genap =",sigmaGenap)
simpson=(fa+4*sigmaGanjil+2*sigmaGenap+fn)*h/3
print("Nilai Hasil Simpson =",simpson)

from sympy import *
z=Symbol('z')
L=91.44
u=0.01
d=0.1
p=1
g=9.81
R=10
a=64*L*u/(p*d**2)
fd=(8*R**2)/(d**2)*(-a+sqrt(a**2+8*g*(z+L)))
integral=fd.integrate(z)
print("Hasil Integral=",integral)

from scipy import integrate
hasilIntegral=integrate.quad(poisel,5,50)
print("Hasil Integral Eksak",hasilIntegral)

er_simson=abs(simpson-hasilIntegral[0])
er_trape=abs(hasil-hasilIntegral[0])
print("Hasil Eror Sympson = ", er_simson)
print("Hasil Eror Trapezoid = ", er_trape)


