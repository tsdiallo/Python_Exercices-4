from random import randint
def tirerLoto (L,x):
    L.append(randint(1,6))
    L.append(randint(6,20))
    L.append(randint(100,300))
    L.append(randint(50,99))
    L.append(randint(3,9))
    L.append(randint(11,32))
    if x in L:
        return True
    else:
        return False
x=int(input("entrer la valeur\t"))
L=[]
boole=tirerLoto(L,x)
print(L)
print(boole)

