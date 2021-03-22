clc
history -c
x=[0.1 0.3 0.5 0.7 0.9 1.1 1.3];
y=[0.030 0.067 0.148 0.248 0.320 0.518 0.697];
xk=[0.365 0.512 0.621 0.715];
n=length(x);
%%%%%
for k=1:4
  sigma(k)=0;
for i=1:n
  L=1;
  for j=1:n
    if j!=i
      L=L*(xk(k)-x(j))/(x(i)-x(j));
    endif
  endfor
  sigma(k)=sigma(k)+y(i)*L;
endfor
endfor
disp("      y(1)       y(2)      y(3)       y(4) ")
disp(sigma)
plot(x,y,'*')