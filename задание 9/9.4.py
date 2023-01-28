A=int(input())
B=int(input())
C=int(input())

S_pr=A*B
S_kv=C**2

print('число квадратов, размещенных на прямоугольнике =', S_pr//S_kv)
print('площадь незанятой части прямоугольника =', S_pr%S_kv)
