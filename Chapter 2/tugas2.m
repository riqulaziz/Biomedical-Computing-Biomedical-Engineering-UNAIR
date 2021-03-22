clc
history -c

function ap=ergun(x)
ap=1.125*x*x-2.348*x+0.8181875;
endfunction
bb=0.1;
ba=0.9;
er=1000;
n=0;
fprintf("iteraasi   x               fba         fbb           fx            eror\n");
while er>0.01
    n=n+1;
    fba=ergun(ba);
    fbb=ergun(bb);
  x=bb-((fbb*(bb-ba))/(fbb-fba));
  f=ergun(x);
  k=fbb*f;
  er=abs(f);
  fprintf("%d        %d,     %d,    %d,    %d,      %d\n",n,x,fba,fbb,f,er);
  if k<0
    ba=x;
    fba=f;
  else
    bb=x;
    fbb=f;
  endif
endwhile
