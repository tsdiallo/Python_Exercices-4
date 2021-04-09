def f(L):
    K=[]
    L.reverse ()
    for i in range( len(L)):
        if (i%3==0):
            K.append (L[i])
    return K
L=[19, 43, 25, 54, 71, 76, 88, 53, 67, 22, 90, 79, 12, 25]        
print L,"->",f(L)

def f(L):
    K=[]
    L.reverse ()
    for i in range( len(L)):
        if (i%3==0):
            K.append (L[i])
    return K
L=[19, 43, 25, 54]       
print L,"->",f(L)

def f(L):
    K=[]
    L.reverse ()
    for i in range( len(L)):
        if (i%3==0):
            K.append (L[i])
    return K
L=[19]       
print L,"->",f(L)


    
