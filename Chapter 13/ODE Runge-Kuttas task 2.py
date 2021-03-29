import numpy as np
import matplotlib.pyplot as mtp
def Runge4(x,y,func,h):
    w1=h*func(x,y)
    w2=h*func(x+0.5*h,y+0.5*h*w1)
    w3=h*func(x+0.5*h,y+0.5*h*w2)
    w4=h*func(x+h,y+h*w3)
    y=y+(w1+2*w2+2*w3+w4)/6
    return y
def sperical(x,y,a=1e-4,rhos=1.1,rhof=1.0,g=981.0,u=3.5e-2):
    y1=y[0]
    y2=(rhos-rhof)*g/rhos-(9/2)*u*y[1]/(a**2)/rhos
    return np.array([y1,y2])
####
TimeBegin=0.0;TimeFinal=0.001
y01=0.0;y02=0.0
y=[y01,y02]
h=eval(input('Masukkan Nilai h = '))
ti=[];y1=[];y2=[]
##
while TimeBegin<TimeFinal:
    y=Runge4(TimeBegin,y,sperical,h)
    TimeBegin+=h
    ti.append(TimeBegin)
    y1.append(y[0])
    y2.append(y[1])
panjang=len(ti)
##Ploting
mtp.subplot(1,2,1)
mtp.plot(ti,y1,'k')
mtp.ylabel('z (um)')
mtp.xlabel('time(s)')
mtp.subplot(1,2,2)
mtp.plot(ti,y2,'k')
mtp.ylabel('v (um/s)')
mtp.xlabel('time(s)')
mtp.show()