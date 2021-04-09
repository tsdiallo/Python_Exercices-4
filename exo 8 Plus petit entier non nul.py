def mini (L,i):
   
    mini=L[i]
    for j in range (i+1,len(L)):
        if(L[j]!=0 and L[j]<mini):
            mini=L[j]
    return mini

L=[40, 10, 50, 20] 
i=0
print L,i,"->",mini (L,i)
            
        
