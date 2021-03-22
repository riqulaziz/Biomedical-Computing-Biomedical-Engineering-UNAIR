clc
history -c

R=0.6;
a=[(2-1.5*R) -0.5;1 -1];
b=[779.3-780*R 76];
x=[0 0];
[m n]= size(a);
ite=0;
ter=1e-3;
er=1;
fprintf("ite       eror x1         eror x2             x1              x2\n")
  while (ite<=100&er>=ter)
  x1=x;
  for i=1:m
    sigma=0;
     for j=1:n
       if j!=i
         sigma=sigma+a(i,j)*x1(j);
       endif
     endfor
     x(i)=(b(i)-sigma)/a(i,i);
  endfor
  er=abs(x1-x);
  ite++;
  fprintf(" %d      %f      %f        %f     %f    \n", ite,er,x(2),x(1));
endwhile