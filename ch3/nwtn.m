clc
history -c

function l=i(x)
  l=x*x*x+x*x+x+1;
endfunction
function k=p(x)
  k=3*x*x+2*x+1;
endfunction

bt=5;
fprintf("iterasi      f(x)         f'(x)                x     \n");
for n=1:6
  fa=i(bt);
  fb=p(bt);
  bt=bt-(fa/fb);
  fprintf("%d         %d          %d            %f\n",n, fa,fb,bt);
endfor
