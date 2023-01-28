K = int(input())
N = int(input())

if K <= 365 and K >= 1 and N <= 7 and N >= 1:
    if N==1:
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

    if N==2:
        if K%7==0:
            print(K, "- понедельник")
        if K%7==1:
            print(K, "- вторник")
        if K%7==2:
            print(K, "- среда")
        if K%7==3:
            print(K, "- четверг")
        if K%7==4:
            print(K, "- пятница")
        if K%7==5:
            print(K, "- суббота")
        if K%7==6:
            print(K, "- воскресенье")

    if N==3:
        if K%7==0:
            print(K, "- вторник")
        if K%7==1:
            print(K, "- среда")
        if K%7==2:
            print(K, "- четверг")
        if K%7==3:
            print(K, "- пятница")
        if K%7==4:
            print(K, "- суббота")
        if K%7==5:
            print(K, "- воскресенье")
        if K%7==6:
            print(K, "- понедельник")

    if N==4:
        if K%7==0:
            print(K, "- среда")
        if K%7==1:
            print(K, "- четверг")
        if K%7==2:
            print(K, "- пятница")
        if K%7==3:
            print(K, "- суббота")
        if K%7==4:
            print(K, "- воскресенье")
        if K%7==5:
            print(K, "- понедельник")
        if K%7==6:
            print(K, "- вторник")

    if N==5:
        if K%7==0:
            print(K, "- четверг")
        if K%7==1:
            print(K, "- пятница")
        if K%7==2:
            print(K, "- суббота")
        if K%7==3:
            print(K, "- воскресенье")
        if K%7==4:
            print(K, "- понедельник")
        if K%7==5:
            print(K, "- вторник")
        if K%7==6:
            print(K, "- среда")

    if N==6:
        if K%7==0:
            print(K, "- пятница")
        if K%7==1:
            print(K, "- суббота")
        if K%7==2:
            print(K, "- воскресенье")
        if K%7==3:
            print(K, "- понедельник")
        if K%7==4:
            print(K, "- вторник")
        if K%7==5:
            print(K, "- среда")
        if K%7==6:
            print(K, "- четверг")

    if N==7:
        if K%7==0:
            print(K, "- суббота")
        if K%7==1:
            print(K, "- воскресенье")
        if K%7==2:
            print(K, "- понедельник")
        if K%7==3:
            print(K, "- вторник")
        if K%7==4:
            print(K, "- среда")
        if K%7==5:
            print(K, "- четверг")
        if K%7==6:
            print(K, "- пятница")    
