clc
clear
%% Jacobi Method
%% Solution of x in Ax=b using Jacobi Method
% * _*Initailize 'A' 'b' & intial guess 'x'*_
%%
A=[2 1 -5;-1 -5 -1;7 -1 -3];
b=[9 14 26];
x=[1 2 2];
n=size(x,1);
normVal=Inf; 
%% 
% * _*Tolerence for method*_
tol=1e-5; itr=0;
%% Algorithm: Jacobi Method
%%
while itr<=1
    xold=x;
    for i=1:n
        sigma=0;
        for j=1:n
            if j~=i
                sigma=sigma+A(i,j)*x(j);
            endif
        endfor
        
        x(i)=(1/A(i,i))*(b(i)-sigma);
    endfor
    
    itr=itr+1;
    normVal=abs(xold-x);
    x
endwhile
%%
fprintf('Solution of the system is : \n%f\n%f\n%f\n%f in %d iterations\n',x,itr);