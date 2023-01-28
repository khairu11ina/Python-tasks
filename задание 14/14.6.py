N = int(input())

pr, Next = 0, 1
n = 1

while Next <= N:
    if Next == N:
        print(n)
        break
    pr, Next = Next, pr + Next
    n += 1
    
else:
    print(-1)
