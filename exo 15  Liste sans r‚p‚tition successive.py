def f(L):
    M=[]
    for i in range (0,len(L)-1) :
        if(L[i] not in M and L[i+1]!= L[i] or L[i]==L[i+1]):
            M.append (L[i])
            
    return M
       
L=[7,0,1]
print L,"->",f(L)
