A = int(input())
B = int(input())

while A != 0 and B != 0:
   if A>B:
       A = A % B
   else:
       B = B % A

print(A + B)
