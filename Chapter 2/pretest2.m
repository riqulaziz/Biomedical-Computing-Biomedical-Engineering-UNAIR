clc
history -c

function y=l(x)
  y=3.2*x*x+0.08*x-4.7;
endfunction
bb=0;
ba=7;
#i=1;
while er>0.001
  fba=l(ba);
  fbb=l(bb);
  x=bb-((fbb*(bb-ba))/(fbb-fba));
  f=l(x);
  k=fbb*f;
  er=abs(f);
  fprintf("n=%d    x=%d,    fba=%d,  fbb=%d, f=%d,    er=%d\n",i,x,fba,fbb,f,er);
  if k<0
    ba=x;
    fba=f;
  else
    bb=x;
    fbb=f;
  endif
end
