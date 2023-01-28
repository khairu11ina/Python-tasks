A=int(input())
B=int(input())
if A!=B:
    if A>B:
        B=A
        print('тк A > B:',"A =",A,'и B =',B)
    else:
        A=B
        print('тк B > A:',"A =",A,'и B =',B)
else:
    A=0
    B=0
    print("тк A = B:","A =",A,'и B =',B)
