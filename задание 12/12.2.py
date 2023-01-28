print('введите C')
C = input()

print('введите N')
N = int(input())

if (C=='С'):
    if (N==0):
        print ('Север')
    elif (N==1):
        print('Запад')
    elif (N==-1):
        print ('Восток')
elif (C == 'З'):
    if (N==0):
        print ('Запад')
    elif (N==1):
        print('Юг')
    elif (N==-1):
        print ('Север')
elif (C == 'Ю'):
    if (N==0):
        print ('Юг')
    elif (N==1):
        print('Запад')
    elif (N==-1):
        print ('Восток')
elif (C == 'В'):
    if (N==0):
        print ('Восток')
    elif (N==1):
        print('Юг')
    elif (N==-1):
        print ('Север')
else:
    print('Ошибка')
