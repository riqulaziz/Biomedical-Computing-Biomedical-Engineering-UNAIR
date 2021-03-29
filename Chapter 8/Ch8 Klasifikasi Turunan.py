import math as mt
def fungsi(x):
    return x*mt.sin(x)
A=[1.2,1.4,1.6,1.8,2.0]
number=eval(input(" masukan nilai x ="))
for i in range (0,len(A)):
    if A[i] >= number:
        urut=i
        break
if number==1.2 :
    h=A[urut]-A[urut-1]
    fow=(fungsi(number+h)-fungsi(number))/h
    print('Hasil dengan metode forward= ',fow)
elif number>1.2 and number<2.0:
    h = A[urut] - A[urut - 1]
    fow = (fungsi(number + h) - fungsi(number))/h
    print('Hasil dengan metode forward= ',fow)
    back=(fungsi(number)-fungsi(number-h))/h
    print('Hasil dengan metode backward = ',back)
    center=(fungsi(number+h)-fungsi(number-h))/2*h
    print('Hasil dengan metode center= ',center)
elif number==2.0:
    h = A[urut] - A[urut - 1]
    back = (fungsi(number) - fungsi(number - h)) / h
    print('Hasil dengan metode backward= ',back)
