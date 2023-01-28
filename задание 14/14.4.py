P=float(input())
K=0
S=1000
if 0<P and P<25:
   while True:
       if S>1100:
           break
       else:
           K+=1
           S=S+S*P/100
   print('вклад превысит 1100 рублей через ', K, ' месяцев ', 'и к этому моменту итоговый размер вклада будет равен ', round(S), ' рублей.', sep='')
else:
   print('mistake!')
