print('введите N')
N=int(input())

S=0.0
for i in range(1, N+1):
    a = 2*i-1
    S+= a
    print(i, ':', S)
print('Sum = ', S)
