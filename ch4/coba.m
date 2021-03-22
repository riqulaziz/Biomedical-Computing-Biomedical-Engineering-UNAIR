clc
history -c

A=[2  -1  3 -1   1  10;
   1  -3  -4  3  1  0;
   3  -1   2  1 -1   6;
   2  -1   1  1  -1   2;
   3   -2  -1  1  1   5];   
C=[10;0;6;2;5];
%%%%%%%%%%%%%
[m n]=size(A);%m=baris; n=kolom
for k=1:m-1 %nilai k menjadi j 
  for i=k+1:m
      A(i,:)=A(i,:)-(A(i,k))/(A(k,k))*A(k,:);
  endfor
endfor
A
%%%%%
p=0;
for i=m-1:1
  for j=2:m
    for k=i+1:m
      p=p+A(k,j)*x(j);
    endfor
  endfor
  x=A(i,n)-p;
endfor
x