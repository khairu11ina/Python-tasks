import math

x1, y1, x2, y2, x3, y3 = list(map(int, input().split()))

a = math.sqrt(pow((x2-x1),2) + pow((y2-y1),2))
b = math.sqrt(pow((x3-x2),2) + pow((y3-y2),2))
c = math.sqrt(pow((x1-x3),2) + pow((y1-y3),2))

p = (a + b + c) / 2
S = math.sqrt(p * (p-a) * (p-b) * (p-c))

print("P =", round(p*2,2))
print("S =", round(S,2))
