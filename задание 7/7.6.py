import numpy

A1=int(input())
B1=int(input())
C1=int(input())
A2=int(input())
B2=int(input())
C2=int(input())

M1 = numpy.array([[A1, B1],[A2, B2]])
V1 = numpy.array([C1, C2])

resh = numpy.linalg.solve(M1,V1)
print(resh)
