N = int(input())
Sum=0

for K in range(1,1000000):
    Sum+=K
    if Sum>N:
        break

print('наименьшее К: 1')
print('сумма  = ', Sum)
