import math as mt
def integrateRichardson(z, L=91.44, u=0.01, d=0.1, p=1, g=981, R=10):
    a=64*L*u/(p*(d**2))
    return (8*(R**2))/(d**2)*(1/(-a+mt.sqrt((a**2)+8*g*(z+L))))
xi=[]
xii=[]
fxi=[]
ai=5
a=ai
b=50
print('\n######## Program Extrapolasi Richardson Integral Metode Trapesium ########\n')
pias=eval(input('Masukan Jumlah pias = '))
hi=(b-a)/pias
hii=hi
fa=integrateRichardson(a)
fn=integrateRichardson(b)
###
while a<b+hi:
    xi.append(a)
    a=a+hi
print('nilai xi =',xi)
panjang=len(xi)
######
layer=int(mt.log10(pias)/mt.log10(2))
print('jumlah layer = ',layer)
print('\nlapisan ke = 1')
for i in range(0,layer):
    xii = []
    a = ai
    hh=hi*(2**i)
    while a<b+hi:
        xii.append(a)
        a=a+hh
        #print('nilai xii=',xii)
    panjang=len(xii)
     ####
    sigma=0
    for i in range(1,panjang):
    #print('Nilai fx =',integrateRichardson(xi[i]))
        sigma=sigma+integrateRichardson(xii[i])
        #print('sigma =',sigma)
     #### Metode Trapezium
    I=(fa+2*sigma+fn)*hh/2
    fxi.append(I)
panjang=len(fxi)
print('panjang fxi =',panjang)
print('nilai I pada layer pertama =',fxi)
####
if panjang>1:
    n=1
    for j in range(1,layer):
        print('\nlapisan ke =',j+1)
        n=j
        Ij=[]
        print('Nilai Perkalian =',n)
        for i in range(0,panjang-1):
            In=fxi[i]+((fxi[i]-fxi[i+1])/(2**n-1))
            Ij.append(In)
        fxi=Ij
        print('Nilai Ij =',Ij)
        panjang=len(fxi)

### Program Trapezoid Biasa ##
a1=5
b1=50
h1=(b1-a1)/pias
isiX=[]
isiY=[]
while a1<b1+h1:
    isiX.append(a1)
    a1+=h1
print('\nNilai x =',isiX)
panjangX = len(isiX)
for i in range (0, panjangX):
    v=integrateRichardson(isiX[i])
    isiY.append(v)
print('Nilai hasil fungsi =',isiY)
panjangY=len(isiY)
###
sigmaTrapez=0
for i in range(1,panjangY-1):
    sigmaTrapez+=isiY[i]
print("sigma =",sigmaTrapez)
## METODE TRAPEZOID
hasil=(fa+2*sigmaTrapez+fn)*h1/2
print("Hasil Trapezoid =", hasil)
###Exact Value
from sympy import *
ak=5852.15999
R=10
d=0.1
L=91.44
g=981
x=Symbol('x')
fd=(8*(R**2))/(d**2)*(1/(-ak+sqrt((ak**2)+8*g*(x+L))))
integral=fd.integrate(x)
print("\nHasil Integral=",integral)

from scipy import integrate
hasilIntegral=integrate.quad(integrateRichardson,5,50)
print("Hasil Integral Eksak",hasilIntegral)

er=abs(Ij[0]-hasilIntegral[0])
erTrape=abs(hasil-hasilIntegral[0])
print('Nilai Eror metode Richardson =', er)
print('Nilai Eror metode Trapezoid biasa =',erTrape)









