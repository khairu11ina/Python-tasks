def Sign(X):
    if X<0:
        return -1
    elif X==0:
        return 0
    else:
        return 1

A = int(input())
B = int(input())

print(Sign(A)+Sign(B))
