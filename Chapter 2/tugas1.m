clc
history -c

function ap=ergun(x)
ap=1.125*x*x-2.348*x+0.8181875;
endfunction
bb=0.1;
ba=0.9;
er=100000;
n=0;
fprintf("Iterasi        x               eror\n");
while er>0.01
    n=n+1;
    fa=ergun(ba);
    fb=ergun(bb);
    x=(ba+bb)/2;
    fx=ergun(x);
    er=abs(fx);
    k=fx*fb;
    fprintf("%d             %d            %f\n",n,x,er);
    if k<0
      ba=x;
      fa=fx;
     else
      bb=x;
      fb=x;
    endif
endwhile