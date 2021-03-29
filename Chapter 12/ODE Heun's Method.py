import math as mt
import matplotlib.pyplot as mtp
def ODE(t,y):
    return 4*mt.exp(0.8*t)-0.5*y
a=0 # batas bawah
ai=a
b=4 #batas atas
h=eval(input('Masukkan jumlah h ='))
#h=(b-a)/N
t=0
w=2
ti=[]
wi=[]
yi=[]
##
while a<b:
    w1=h*ODE(t,w)
    w2=h*ODE(t+h,w1+w)
    w=w+(w1+w2)/2
    a=a+h
    t = a
    y=(4*(mt.exp(0.8*t)-mt.exp(-0.5*t))/1.3)+2*mt.exp(-0.5*t)
    eror=abs(y-w)
    ti.append(t)
    wi.append(w)
    yi.append(y)
    print('nilai t =',t,'nilai w =',w, 'nilai y =',y, 'eror =',eror)
mtp.plot(ti,wi,'g-',ti,yi,'k-')
mtp.xlabel('t (sekon)')
mtp.ylabel(" y' ")
mtp.title('Grafik Metode Euler')
#mtp.show()



