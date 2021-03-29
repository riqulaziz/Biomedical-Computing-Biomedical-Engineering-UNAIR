import math as mt
import matplotlib.pyplot as mtp
def RLC(t,q,e=12,C=5e-6,R=8e5):
    return (e/R)-(q/(R*C))
def Exact(t,C=5e-6,e=12,R=8e5):
    return C*e*(1-mt.exp(-t/(R*C)))
t1=0;t2=2;
h=0.1
t=0;q=0;
er=[];ti=[];qi=[];yi=[]
print('\n ####Metode Runge-Kutta 4th Orde ####\n')
#Runge kuta orde 4
while t1<t2:
    q1=h*RLC(t,q)
    q2=h*RLC(t+0.5*h,q+0.5*q1*h)
    q3=h*RLC(t+0.5*h,q+0.5*q2*h)
    q4=h*RLC(t+h,q+h*q3)
    q=q+(q1+2*q2+2*q3+q4)/6
    t1+=h
    t=t1
    y=Exact(t)
    eror=abs(y-q)
    ti.append(t)
    qi.append(q)
    yi.append(y)
    er.append(eror)
panjang=len(ti)
print('Nilai t =',ti,'\nNilai q =',qi,'\nNilai eksak =',yi,'\nNilai eror =',er)
print('Nilai q pada t =2 adalah ',qi[panjang-1],'\nSedangkan nilai eksaknya pada t=2 adalah',yi[panjang-1])
print('Nlai eror pada t=2 adalah ',er[panjang-1])
#ploting
mtp.plot(ti,qi,'g*',ti,yi,'k')
mtp.title('Grafik Hasil Runge-Kutta Orde 4')
mtp.xlabel('time(s)')
mtp.ylabel('Voltage (v)')
mtp.show()