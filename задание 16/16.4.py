mas = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]
mass = []

for i in range(len(mas) // 2):
    mass.append(mas[i])
    mass.append(mas[len(mas) - i - 1])
if len(mas) % 2 != 0:
    mass.append(mas[len(mas) // 2])

print(mass)
