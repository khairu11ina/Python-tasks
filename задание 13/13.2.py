print('введите N')
N=int(input())

S=1.0
for i in range(1,N+1):
    x=1+0.1*i
    S*=x
    print(i, ':', x, ':', S)
print('Ответ = ', S)
