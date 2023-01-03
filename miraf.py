from random import shuffle , randint
from string import ascii_letters , digits , punctuation

list = []

xarif = int(input("nechta xarif : "))
belgi = int(input("nechta belgi: "))
raqam = int(input("nechta raqam: "))






for xarif in range(0, xarif):
    x = randint( 0 , 53)
    xar = ascii_letters[x]
    list.append(xar)

for belgi in range(0, belgi):
    b = randint(0, 33)
    bel = punctuation[b]
    list.append(bel)

for raqam in range(0, raqam):
    r = randint(0 ,10)
    list.append(r)

shuffle(list)

parol = ""
for  p in list:
    parol = parol + str(p)

print(parol)


