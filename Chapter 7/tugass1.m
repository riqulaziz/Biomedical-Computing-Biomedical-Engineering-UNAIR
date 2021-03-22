clc
clear
syms x;
xi=[0.1 0.3 0.5 0.7 0.9 1.1 1.3];
yi= [0.030 0.067 0.148 0.248 0.320 0.518 0.697];
n=length(xi);
fx=0;
for i=1:n
    qx=1;
    for j=1:n
        if (i~=j)
            qx=qx*(x-xi(j))/(xi(i)-xi(j));
        end
    end
   qx1=subs(qx,x,xi(i));
   lx=qx/qx1;
   lk1=collect(lx);
   fprintf("L%d(x)= ", i)
   disp(lk1)
   fx=fx+yi(i)*lx;
end
px=collect(fx);
fprintf("bentuk umum polinom lagrangnya =")
disp(px)
c=0.1:0.001:1.5;
f=inline(px);
k=f(c);
plot(xi,yi,'*',c,k)
title("Plot Interpolasi dengan Batas Tidak Sesuai")
xlabel("x(n)")
ylabel("y(n)")


