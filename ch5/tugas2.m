clc
clear
%Jacobi iteration method
a=[0.36 0.51 0.13;
  0.52 0.34 0.74;
  0 0.07 0.11;];
b=[33 45 3];
x=[3 2 1];
[m n]=size(a);
ite=0;
ter=1e-3;
er=1;
fprintf("ite       eror x1         eror x2      eror x3            x1               x2              x3\n")
  while (ite<20&er>=ter)
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
  fprintf(" %d      %f      %f     %f    %f     %f       %f\n", ite,er,x(1),x(2),x(3));
endwhile
