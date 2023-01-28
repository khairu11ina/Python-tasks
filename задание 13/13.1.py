print('Введите цену 1 кг конфет')
price=int(input())

print()
for i in range (1, 11):
    x=0.1*i
    print('Стоимость {0:.1f} кг: {1:.2f}'.format(x, x * price))
print()
