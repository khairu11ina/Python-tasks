A = int(input())
B = int(input())
C = int(input())
         
AB = abs(A-B)
AC = abs(A-C)
         
print("Расстояние от A до B =",AB)
print("Расстояние от A до C =",AC)
         
if AB > AC:
    print("к A ближе C")
elif AB < AC:
    print("к A ближе В")
else:
    print("B и C равноудалены от A")
