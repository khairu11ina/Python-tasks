print('введите N')
N=int(input())
mas=[]
i=1

while len(mas)!=N:
    if i%2==1:
        mas.append(i)
    i=i+1

print(mas)
