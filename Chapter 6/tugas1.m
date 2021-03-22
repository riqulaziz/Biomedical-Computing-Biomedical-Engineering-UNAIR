clc
history -c

x=[ 8 17 20 25 31 42 50 59 65 72 80];
y=[100 130 209 276 330 359 420 487 550 645 700];
n=length(x);
%Inisialisasi sigma
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
plot(x,y,'*',x,fungsi)
xlabel("x")
ylabel("y / fungsi fx")