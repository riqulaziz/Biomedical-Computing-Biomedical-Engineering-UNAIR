import math as mt
def velocity(t,g=9.8,m=78.5,c=12.5):
    return (g*m*(1-mt.exp(-(c/m)*t)))/c
ti=[]
t0=0 # Waktu Awal
t1=12 # Waktu Akhir
n=12000
h=(t1-t0)/n
fa=velocity(t0)
fn=velocity(t1)
## pengisian matriks
while t0<t1+h:
    ti.append(t0)
    t0=t0+h
print('nilai t=',ti)
panjang=len(ti)
####
velo=[]
for i in range (0, panjang):
    v=velocity(ti[i])
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
t=Symbol('t')
g=9.8
m=78.5
c=12.5
fd=(g*m*(1-exp(-(c/m)*t)))/c
integral=fd.integrate(t)
print("Hasil Integral=",integral)

from scipy import integrate
hasilIntegral=integrate.quad(velocity,0,12)
print("Hasil Integral Eksak",hasilIntegral)

er_simson=abs(simpson-hasilIntegral[0])
er_trape=abs(hasil-hasilIntegral[0])
print("Hasil Eror Sympson = ", er_simson)
print("Hasil Eror Trapezoid = ", er_trape)


