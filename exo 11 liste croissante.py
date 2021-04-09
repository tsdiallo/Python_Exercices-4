def est_croissante (L):
    cpt=0
    for i in range (0,len(L)-1):
        if (L[i]<=L[i+1]):
            cpt=cpt+1
    if (cpt==len(L)-1):
        return True
    else:
         return False
        
L=[5, 6, 6, 6, 10]

print (est_croissante (L))

