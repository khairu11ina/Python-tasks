def Quarter(x,y):
    if x>0:
        if y>0:
            print('точка находится в первой четверти')
        elif y<0:
            print('точка находится в четвертой четверти')
        else:
            print('одна из координат равна нулю')
    elif(x<0):
        if y>0:
            print('точка находится во второй четверти')
        elif y<0:
            print('точка находится в третьей четверти')
        else:
            print('одна из координат равна нулю')
    else:
        print('одна из координат равна нулю')

print('введите две координаты первой точки')
a2=int(input())
b2=int(input())
print(Quarter(a2,b2))

print('введите две координаты второй точки')
a1=int(input())
b1=int(input())
print(Quarter(a1,b1))

print('введите координаты третьей точки')
a3=int(input())
b3=int(input())
print(Quarter(a3,b3))
