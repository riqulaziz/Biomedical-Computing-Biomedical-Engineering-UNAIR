clc
history -c

a= [2  -1  3 -1   1 ;
   1  -3  -4  3  1  ;
   3  -1   2  1 -1   ;
   2  -1   1  1  -1   ;
   3   -2  -1  1  1   ]
c=[10;0;6;2;5];
%%---------SEGITIGA ATAS--------------
[m n]=size(a);
for eli=1:m-1
  for i=eli+1:m
    pivot=(a(i,eli)/a(eli,eli));
    for j=1:n
      a(i,j)=a(i,j)-pivot*a(eli,j);
    endfor
    c(i)=c(i)-pivot*c(eli);
  endfor
endfor
a
%%-------------SUBTITUSI BALIK-----------
x(5)=c(5)/a(5,5);
for i=4:-1:1
  sigma=0;
  for j=i+1:m
    sigma=sigma+a(i,j)*x(j);
  endfor
  x(i)=(c(i)-sigma)/a(i,i);
endfor
fprintf("     x1         x2        x3        x4        x5\n");
disp(x)