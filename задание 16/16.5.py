mas = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
mass = []

for i in mas:
    if i%2!=0:
        mass.append(mas[i])
for i in reversed(mas):
    if i%2==0:
        mass.append(mas[i])

print(mass)
