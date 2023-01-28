x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

if x2 > x1:
    a = x2 - x1
else:
    a = x1 - x2

if y2 > y1:
    b = y2 - y1
else:
    b = y1 - y2

S = a * b
P = 2 * (a + b)

print("S =", abs(S))
print("P =", abs(P))
