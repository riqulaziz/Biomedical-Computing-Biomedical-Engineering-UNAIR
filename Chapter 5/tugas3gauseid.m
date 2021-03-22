clc
history -c

a=[1 1 1 0 0 0; 0 -1 0 1 -1 0; 0 0 -1 0 0 1;
  0 0 0 0 1 -1; 0 10 -10 0 -15 -5; 5 -10 0 -20 0 0];
b=[0 0 0 0 0 200];
x=[2 3 5 2 10 7];
[m n]= size(a);
ite=1;
ter=1e-3;
er=1;
  while (ite<=100&er>=ter)
  x1=x;
    for i=1:m
      sigma=0;
      for j=1:n
        if j!=i
          sigma=sigma+a(i,j)*x(j);
        endif
      endfor
      x(i)=(b(i)-sigma)/a(i,i);
    endfor
  er=abs(x1-x);
  ite++;
endwhile
ite
er
x