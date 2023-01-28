print('введите A')
A=float(input())

print('введите N')
N=int(input())

s=0

for i in range(N+1):
    s+= (-1)**i * A**i

print("Sum = ", s)
