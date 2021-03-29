import math as mt
def derivRichardson(x):
    return x**(2)+mt.cos(x)
xi=[]
fxi=[]
a=0
b=2
h=0.01
hi=h
######
print("Nama : M. Thoriqul Aziz\n NIM = 081711733002 ")
while a<b+h:
    xi.append(a)
    a=a+h
print('nilai x = ',xi)
panjang=len(xi)
####
for i in range(0,panjang):
    fx=derivRichardson(xi[i])
    fxi.append(fx)
#print('Nilai fx=', fxi)
#####
num=eval(input('Masukan nilai x ='))
for i in range (0,panjang):
    if xi[i] >= num:
        urutan=i
        break
print('urutan keberapa = ', urutan)
lapisan=int(mt.log10(urutan)/mt.log10(2))
print('Jumlah Lapisan = ',lapisan)
####
Di=[]
print('Lapisan ke 1')
for i in range(0,lapisan+1):
    lapis=2**i
    x0=xi[urutan-lapis]
    x1=xi[urutan+lapis]
    D=(derivRichardson(x1)-derivRichardson(x0))/(2*h*lapis)
    Di.append(D)
print("Nilai semua D",Di)
panjangDi=len(Di)
####
if panjangDi>1:
    n=1
    for j in range(1,lapisan+1):
        print('Lapisan ke ',j+1)
        n=2*j
        Dj=[]
        print('Jumlah perkalian h =',n)
        for i in range (0,panjangDi-1):
            #print(Di[0],Di[1])
            Der=Di[i]+((Di[i]-Di[i+1])/(2**n-1))
            Dj.append(Der)
        Di=Dj #pengubah dalam perhitungan der
        print('Nilai Dj = ',Di)
        panjangDi=len(Di)
######
### Perhitungan dengan Metode Center
# Nilaix=num
# print('hasil num =', num)
# D2h=(derivRichardson(Nilaix+0.2) - derivRichardson(Nilaix-0.2))/0.4
# D4h=(derivRichardson(Nilaix+0.4) - derivRichardson(Nilaix-0.4))/0.8
# center=D2h+(D2h-D4h)/15
# print('Hasil metode center =', center)
######
from sympy import *
x=Symbol("x")
fd=x**(2)+cos(x)
dydx=fd.diff(x)
print("turunan pertama =",dydx)
####### Mengetahui Hasil Sebenarnya dari Perhitungan Turunan Kontinu ########
fx=lambdify(x,dydx)
print("f'(",num,")=",fx(num))
er=abs(fx(num)-Di)
# er1=abs(fx(num)-center)
print("Nilai Eror dari hasil perhitungan dengan Metode Richardson =", er)
# print('Nilai eror dibandingkan dengan metode center =',er1)