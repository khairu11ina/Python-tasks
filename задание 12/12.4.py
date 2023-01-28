A = int(input())

a = int(A%10)
b = int((A%100-a)/10)
b_c = int(A%100-a)
c = int((A%1000-b_c-a)/100)

x=' '

mas_c = ['','сто','двести','триста','четыреста','пятьсот','шестьсот','восемьсот','девятьсот']
mas_b = ['','','двадцать','тридцать','сорок','пятьдесят','шестьдесят','семьдесят','восемьдесят','девяносто']
mas_a = ['','один','два','три','четыре','пять','шесть','семь','восемь','девять']

if b==1:
    if a==0:
        print(mas_c[c], 'десять')
    elif a==1:
        print(mas_c[c],'одиннадцать')
    elif a==2:
        print(mas_c[c],'двенадцать')
    elif a==3:
        print(mas_c[c],'тринадцать')
    elif a==4:
        print(mas_c[c],'четырнадцать')
    elif a==5:
        print(mas_c[c],'пятнадцать')
    elif a==6:
        print(mas_c[c],'шестнадцать')
    elif a==7:
        print(mas_c[c],'семнадцать')
    elif a==8:
        print(mas_c[c],'восемнадцать')
    elif a==9:
        print(mas_c[c],'девятнадцать')
elif b==0:
    if a==0:
        print(mas_c[c])
    else:
        print(mas_c[c], x, mas_a[a])
else:
    print(mas_c[c], x, mas_b[b], x, mas_a[a])
