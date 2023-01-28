A = int(input())
B = int(input())
C = int(input())

if C > A:
    AC = C - A
else:
    AC = A - C

if B > C:
    BC = B - C
else:
    BC = C - B

print("AC =", AC)
print("BC =", BC)
print("AC + BC =", AC+BC)
