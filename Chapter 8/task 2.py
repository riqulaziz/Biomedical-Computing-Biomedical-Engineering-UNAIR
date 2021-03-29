from sympy import *
A=[1.2,1.4,1.6,1.8]
B=[0.8333,0.7143,0.6250,0.5556]
number=eval(input(" masukan nilai x ="))
for i in range (0,len(A)):
    if A[i] >= number:
        urut=i
        break
h = A[urut] - A[urut - 1]
print(urut)
fow=(B[urut+1]-B[urut])/h
print("hasil fow =", fow)