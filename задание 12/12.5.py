print('')
Year=int(input())

ani = abs(Year-1984) % 12
col = (abs(Year-1984) // 12) % 5

animal=['Крысы','Коровы','Тигра','Зайца','Дракона','Змеи','Лошади','Овцы','Обезьны','Курицы','Собаки','Свиньи']

if ani==0 or ani==1 or ani==5 or ani==6 or ani==7 or ani==8 or ani==9 or ani==10 or ani==11 :
    if col == 0:
        print(Year,'- год Зеленой', animal[ani])
    elif col == 1:
        print(Year,'- год Красной', animal[ani])
    elif col == 2:
        print(Year,'- год Желтой', animal[ani])
    elif col == 3:
        print(Year,'- год Белой', animal[ani])
    elif col == 4:
        print(Year,'- год Черной', animal[ani])
else:
    if col == 0:
        print(Year,'- год Зеленого', animal[ani])
    elif col == 1:
        print(Year,'- год Красного', animal[ani])
    elif col == 2:
        print(Year,'- год Желтого', animal[ani])
    elif col == 3:
        print(Year,'- год Белого', animal[ani])
    elif col == 4:
        print(Year,'- год Черного', animal[ani])
    
    
