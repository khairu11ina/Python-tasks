print("введите N")
N = int(input())
print("введите A")
A = int(input())
print("введите B")
B = int(input())

mas = [A,B]
for i in range(2,N):
    x = mas[i-2] + mas[i-1]
    mas.append(x)
print(mas)
