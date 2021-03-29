import numpy as np
import matplotlib.pyplot as mtp
y0=10.0;y1=100.0;y2=0.0
y=[y0,y1,y2]
h=0.1
a=0
b=5
t=0
ti=[];yi0=[];yi1=[];yi2=[];
def Virus(time,y):
     w0=0.050*y[1]-0.50*y[0]
     w1=-3.0*y[1]
     w2=30.0*y[0]-3.0*y[2]
     return np.array([w0,w1,w2])

while a<b:      #Perulangan Metode Euler
    y=y+h*Virus(t,y)
    a+=h
    t=a
    ti.append(a)
    yi0.append(y[0])
    yi1.append(y[1])
    yi2.append(y[2])
panjang=len(yi0)
print('Nilai T* saat t=5 hari =',yi0[panjang-1])
print('Nilai V1 saat t=5 hari =',yi1[panjang-1])
print('Nilai Vx saat t=5 hari =',yi2[panjang-1])
## Ploting##
mtp.figure(1)
mtp.subplot(1,3,1)
mtp.plot(ti,yi0,'k')
mtp.ylabel('T* infected cells( Ul )')
mtp.xlabel('t(days)')
mtp.subplot(1,3,2)
mtp.plot(ti,yi1,'k')
mtp.ylabel('V1 virions ( Ul )')
mtp.xlabel('t(days)')
mtp.subplot(1,3,3)
mtp.plot(ti,yi2,'k')
mtp.ylabel('Vx non-infctious virus perticles ( Ul )')
mtp.xlabel('t(days)')
mtp.show()