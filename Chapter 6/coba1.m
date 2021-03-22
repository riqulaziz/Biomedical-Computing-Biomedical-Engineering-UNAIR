clc
history -c

x=[ 1 3 5 7 10 12 13 16 18 20];
y=[3 2 6 5 8 7 10 8 12 10];
n=length(x);

%jumlah x
sigmax=0;
for i=1:n
  sigmax=sigmax+x(i);
endfor
sigmax;

%jumlah y
sigmay=0;
for i=1:n
  sigmay=sigmay+y(i);
endfor
sigmay;

%jumlah xy
sigmaxy=0;
for i=1:n
  sigmaxy=sigmaxy+x(i)*y(i);
endfor
sigmaxy;

%jumlah xx
sigmaxx=0;
for i=1:n
  sigmaxx=sigmaxx+x(i)*x(i);
endfor
sigmaxx;

parameter = inv([sigmaxx sigmax;sigmax n])*[sigmaxy;sigmay];
a = parameter(1);
b = parameter(2);
fungsi = a*x + b;
plot(x,y,'*',x,fungsi)
