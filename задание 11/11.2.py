a,b,c = list(map(int, input().split()))
if (a<=c and a<=b):
    print(b+c)
elif (b<=c and b<=a):
    print(a+c)
else:
    print(a+b)
