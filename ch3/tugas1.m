clc
history -c

function y=u(x)
  y=0.0039*x*x*x-0.78*x*x+39.9*x-467;
endfunction
function yy=uu(x)
  yy=0.0117*x*x-1.56*x+39.9;
endfunction
%Y=x
x=45;%years
er=1;%eror awalan
ter=0.0001;%toleransi eror
n=1;maxit=10;%iterasi dan maximum iterasi
fprintf("iterasi      tebakan akar       eror\n")
while (er>ter&&n<maxit)
  x=x-(u(x)/uu(x));
  er=abs(u(x));
  fprintf("   %d          %f      %f\n",n,x,er);
  n=n+1;
endwhile
