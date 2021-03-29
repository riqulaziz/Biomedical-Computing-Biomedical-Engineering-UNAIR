import math as mt
def RLC(q,t,e=12,C=5e-6,R=8e5):
    return (e/R)-(q/(R*C))
ta=0
taa=ta
tb=2
h=0.1
t=0
tt=t
qe=0
er=[];ti=[];qi=[];yi=[]
print('\n ####Metode Euler####\n')
#Euler Method
while ta<tb:
    qe=qe+h*RLC(qe,t)
    ta+=h
    t=ta
    y=5e-6*12*(1-mt.exp(-t/(8e5*(5e-6))))
    eror=abs(qe-y)
    ti.append(t)
    qi.append(qe)
    yi.append(y)
    er.append(eror)
print('Nilai t =',ti,'\n Nilai q =',qi,'\n Nilai eksak =',yi,'\n Nilai eror =',er)
#Heuns Method
print('\n ####Metode Heun####\n')
qe1=0
er1=[]
ti1=[]
qi1=[]
yi1=[]
while taa<tb:
    qe1Pertama=h*RLC(qe1,tt)
    qe1Kedua=h*RLC(qe1Pertama+qe1,tt+h)
    qe1+=(qe1Pertama+qe1Kedua)/2
    taa+=h
    tt=taa
    y1=5e-6*12*(1-mt.exp(-tt/(8e5*(5e-6))))
    err=abs(qe1-y1)
    ti1.append(tt)
    qi1.append(qe1)
    yi1.append(y1)
    er1.append(err)
print('Nilai t =',ti1,'\n Nilai q =',qi1,'\n Nilai eksak =',yi1,'\n Nilai eror =',er1)
## Ploting##
import matplotlib.pyplot as mtp
mtp.plot(ti,qi,'go',ti,qi1,'k*',ti,yi,'r')
mtp.xlabel('t (sekon)')
mtp.ylabel(" y' ")
mtp.title('Grafik Perbandingan Metode Euler dan Heun')
mtp.show()