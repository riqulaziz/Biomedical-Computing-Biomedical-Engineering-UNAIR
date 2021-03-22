clc
clear
%Gauss seidel iteration method
a=[0.36 0.51 0.13;
  0.52 0.34 0.74;
  0 0.07 0.11;];
b=[33 45 3];
x=[3 2 3];
[m n]=size(a);
ite=1;
while(ite<=2)
    for i=1:m
      sigma=0;
      for j=1:n
        if j!=i
          sigma=sigma+a(i,j)*x(j);
        endif
      endfor
      x(i)=(b(i)-sigma)/a(i,i);
    endfor
 x
 ite++;
endwhile

