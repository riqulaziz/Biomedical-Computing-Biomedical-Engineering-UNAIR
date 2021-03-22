clear
clc

R=0.6:0.05:0.95;
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
x(2)=b(2)/a(2,2);
for i=1:1
  sigma=0;
  for j=2:2
    sigma=sigma+a(i,j)*x(j);
  endfor
  x(i)=(b(i)-sigma)/a(i,i);
endfor
x(1);
