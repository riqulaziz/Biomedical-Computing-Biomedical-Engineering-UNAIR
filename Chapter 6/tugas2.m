clc
history -c

po=[10 20 30 40 50 60 70 80 90 100 110 120];
s=[0.18 0.4 0.65 0.8 0.87 0.92 0.94 0.95 0.95 0.96 0.96 0.97];
n=length(po)
%%%%% di lienierkan %%%%%%%%%%
for i=1:n
  y(i)=log(s(i)/(1-s(i)));
  x(i)=log(po(i));
endfor
y
x
%%%%%%%% inisialisasi sigma%%%%%%%%
sigmay=0;
sigmax=0;
sigmaxy=0;
sigmaxx=0;
for i=1:n
  sigmax=sigmax+x(i);
  sigmay=sigmay+y(i);
  sigmaxx=sigmaxx+x(i)*x(i);
  sigmaxy=sigmaxy+x(i)*y(i);
endfor
parameter = inv([sigmaxx sigmax;sigmax n])*[sigmaxy;sigmay];
a = parameter(1);
b = parameter(2);
fungsi = a*x + b;
figure(1)
subplot(2,1,1)
plot(x,y,'*',x,fungsi)
title("Grafik fungsi linearisasi dan regresi liniernya")
xlabel("x")
ylabel("y / fungsi fx")
subplot(2,1,2)
plot(po,s,'*')
title("Grafik fungsi belum linier")
xlabel("po")
ylabel("s")
p50=e.^(-b/a)