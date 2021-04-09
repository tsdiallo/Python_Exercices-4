L= [-1, 0, -1, 0, 0, 1, -1, 0]
d1=""
def afficherDirection(L):
    for i in range(len(L)):
        if (L[i]== -1):
            d1="A gauche"
        elif(L[i]== 0):
            d1="Tout droit"
        elif(L[i]== 1):
            d1="A droite"
        print(d1)
    return d1

d1=afficherDirection(L)





        
