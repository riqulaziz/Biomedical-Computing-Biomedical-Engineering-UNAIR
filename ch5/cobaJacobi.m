clear
clc

##a = [1.48   0.93   -1.3 ;
##    2.68  3.04   -1.48  ;
##    2.51  1.48  -4.53];
##  
##b=[1.03;  -0.53;  0.05];
##x=[0;0;0];
a = [2   1   -5 ;
    1  -5   -1  ;
    7  -1  -3];
  
b=[9;  14;  26];
x(1)=1;
x(2)=2;
x(3)=2;
[m n]=size(a);
er=1e-5;
ite=1;
while ite<=1
  for i=1:m
    jacob=0;
    for j=1:n
      if j=i
        if j<n
          j=j+1;
      else
        j=j;
      endif
      endif
      jacob=jacob + a(i,j)*x(j);
    endfor
    x(i)=(b(i)-jacob)/a(i,i);;
  endfor
  x
  ite=ite+1;
 % er=abs(xold-x);
endwhile
