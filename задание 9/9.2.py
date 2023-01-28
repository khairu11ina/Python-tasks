K = int(input())
if K <= 365 and K >= 1:
    if K%7==0:
        print(K, "- воскресенье")
    if K%7==1:
        print(K, "- понедельник")
    if K%7==2:
        print(K, "- вторник")
    if K%7==3:
        print(K, "- среда")
    if K%7==4:
        print(K, "- четверг")
    if K%7==5:
        print(K, "- пятница")
    if K%7==6:
        print(K, "- суббота")
        
