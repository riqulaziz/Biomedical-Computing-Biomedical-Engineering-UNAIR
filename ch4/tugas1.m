clear
clc
z=1;
for R=0.6:0.05:0.95
  a=[ 0.5*R   1.5*R-3.238157;
  16.7353 -0.5];
b=[-0.7;2.8175];
%%---------SEGITIGA ATAS--------------
[m n]=size(a);
for eli=1:m-1
  for i=eli+1:m
    pivot=(a(i,eli)/a(eli,eli));
    for j=1:n
      a(i,j)=a(i,j)-pivot*a(eli,j);
    endfor
    b(i)=b(i)-pivot*b(eli);
  endfor
endfor
a;
b;
%%-------------SUBTITUSI BALIK-----------
x(m)=b(m)/a(m,m);
for i=m-1:-1:1
  sigma=0;
  for j=i+1:m
    sigma=sigma+a(i,j)*x(j);
  endfor
  x(i)=(b(i)-sigma)/a(i,i);
endfor
fprintf("\nketika n= ");
disp(R)
fprintf("x1= ");
disp(x(1))
fprintf("x2= ");
disp(x(2))
R1(z)=R;
x1(z)=x(1);
x2(z)=x(2);
z++;
endfor
subplot(2,1,1)
plot(R1,x1,"r")
title("Kurva values of epoxide in the liver")
xlabel("fraction")
ylabel("concentration of epoxide")
ylim([0.177 0.184])
subplot(2,1,2)
plot(R1,x2,"b")
title("Kurva values of epoxide in the lung")
xlabel("fraction")
ylabel("concentration of epoxide")
ylim([0.3 0.45])
