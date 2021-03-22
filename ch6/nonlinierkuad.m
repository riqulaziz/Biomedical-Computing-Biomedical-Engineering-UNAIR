clc
history -c
x=[ 8 17 20 25 31 42 50 59 65 72 80];
y=[100 130 209 276 330 359 420 487 550 645 700];
n=length(x);
%Inisialisasi sigma
sigma4x=0;
sigma3x=0;
sigma2x=0;
sigmax=0;
sigmax2y=0;
sigmaxy=0;
sigmay=0;
for i=1:n
    sigma4x=sigma4x+x(i).^4;
    sigma3x=sigma3x+x(i).^3;
    sigma2x=sigma2x+x(i).^2;
    sigmax=sigmax+x(i);
    sigmax2y=sigmax2y+x(i)*x(i)*y(i);
    sigmaxy=sigmaxy+x(i)*y(i);
    sigmay=sigmay+y(i);
endfor
par = inv([sigma4x sigma3x sigma2x;sigma3x sigma2x sigmax;sigma2x sigmax n])*[sigmax2y;sigmaxy;sigmay];
a = par(1);
b = par(2);
c = par(3);
fungsi=a*(x.*x) + b*x + c;
plot(x,y,'*',x,fungsi)
xlabel("x")
ylabel("y / fungsi fx")