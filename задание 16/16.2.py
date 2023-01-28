print("введите N")
N = int(input())
print("введите A")
A = int(input())
print("введите B")
D = int(input())

mas1 = []
for i in range(N):
    x = A * (D**i)
    mas1.append(x)
#print(mas1)
mas2 = [A * (D**i) for i in range(N)]
print(mas2)
