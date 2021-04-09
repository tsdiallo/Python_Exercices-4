def rempl_neg (L):
   
    for i in range (0,len(L)):
        if(L[i]<0):
            L[i]=L[i]*-1
    return L 
L=[-6, 2, 5, -3, 0, 2, 0, -1]
print (L,"->",rempl_neg (L) )
