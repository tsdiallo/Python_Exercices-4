import random
t=[50,1,2,60,3,5]
def maxi(t,p):
    maxi=t[0]
    max_indice=0
    for i in range(1,p+1):
        if t[i]>maxi:
            maxi=t[i]
            max_indice=i
    return max_indice
def echange(t,i,j):
    t[i],t[j]=t[j],t[i]
def selection(t):
    p=len(t)-1
    while (p>0):
        i=maxi(t,p)
        echange(t,i,p)
        p-=1

print("Avant le tri par selection",t)
selection(t)
print("Apre le tri par selection",t)

l=[]
for i in range (3000):
    l.append(random.randrange(0.1000))

print(l)
selection(l)
print(l)
