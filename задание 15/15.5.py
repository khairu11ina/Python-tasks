print("Введите N ")
N=int(input())

def Fact2(N):
    a=1
    if N%2==0: 
        b = 2
        while b <= N:
            a = a * b
            b = b + 2 
        print(a)
    else:
        b = 3 
        while b <= N:
            a = a * b
            b = b + 2
        print(a)
    
print (Fact2(N))
    
