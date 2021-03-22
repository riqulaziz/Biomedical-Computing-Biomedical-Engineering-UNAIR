clc
history -c
function y=l(x)
  y=3.2*x*x+0.08*x-4.7;
endfunction
bb=0;
ba=7;
i=0;
for i= 1:10
  x=(bb+ba)/2;
  fba=l(ba);
  fbb=l(bb);
  f=l(x);
  k=fbb*f;
  er=abs(f);
  fprintf("x=%d   ,f=%d,      er=%d\n",x,f,er);
  if k<0
    ba=x;
    fba=f;
  else
    bb=x;
    fbb=f;
  endif
end
