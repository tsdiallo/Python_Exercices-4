L=[12, 81, 65, 9, 32]
mini=L[0]
maxi=L[0]
L2=[]
for i in range(len(L)-1):
    if L[i]<mini: 
        mini=L[i]
        L2.append(mini)
        
    if L[i]>maxi:
        maxi=L[i]
        L2.append(maxi)
print(L2)
   
