clc
clear
syms x;
m=[0.1 0.3 0.5 0.7 0.9 1.1 1.3];
x1=0.1:0.1:1.3;
y=[0.030 0.067 0.148 0.248 0.320 0.518 0.697];
%xk=[0.365 0.512 0.621 0.715];
n=length(x);
%%%%%

fx=0;
for i=1:n
  L=1;
  for j=1:n
    if j~=i
      L=L*(x-m(j))/(m(i)-m(j));
    end
  end
  L1=subs(L,x,m(i));
  lx=L/L1;
  lxl=collect(lx)
  fprintf('L%d(x) = ',i)
  disp(lxl)
  fx=fx+y(i)*lx
end
    
px=collect(fx);
fprintf('\n Hasilnya =');
disp(px);