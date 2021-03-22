clc
clear

a= [2  -1  3 -1   1 ;
   1  -3  -4  3  1  ;
   3  -1   2  1 -1   ;
   2  -1   1  1  -1   ;
   3   -2  -1  1  1   ]
c=[10;0;6;2;5];

%for eli=1:1
  for i=2:2
    for k=1:2
      a(i,k)=a(i,k)-(a(i,1)/a(1,1))*a(1,k);
    end
  end
a