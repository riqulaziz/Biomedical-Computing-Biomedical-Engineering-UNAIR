clc
clear
a = [1.48   0.93   -1.3 ;
    2.68  3.04   -1.48  ;
    2.51  1.48  -4.53];
b=[1.03;  -0.53;  0.05];
x=[0;0;0];
[m n]=size(a);
er=1e-5;
ite=1;
while ite<=5
  xbf=x;
  for i=1:m
    sigma=0;
    for j=i+1:m
      sigma=sigma+a(i,j)*xbf(j);
    endfor
    for j=i:m
      if j=i
        if j<n
          j=j+1;
         else
        j=j; 
      endif
      endif
      sigma=sigma+a(i,j)*x(j)
    endfor
    x(i)=(b(i)-sigma)/a(i,i);
  endfor
  ite++;
  er=abs(xbf-x);
endwhile