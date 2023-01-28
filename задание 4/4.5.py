a = int(input())
b = int(input())
if a>0:
    mod_a = a
else:
    mod_a = a * -1

if b>0:
    mod_b = b
else:
    mod_b = b * -1

summ = mod_a + mod_b
razn = mod_a - mod_b
proizv = mod_a * mod_b
chastn = mod_a / mod_b

print(summ, razn, proizv, chastn)
