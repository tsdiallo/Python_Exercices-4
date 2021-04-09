def aucunMultiple10(L):
    aucunmultiple=True
    for i in range (0,len(L)):
        if (L[i]%10==0):
            aucunmultiple=False
    return aucunmultiple
L=[42, 81, 33, 81,90]
print (L,"->",aucunMultiple10(L))

