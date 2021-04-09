n=int(input("Entrez n "))
p=int(input("Entrez p "))
def Factorielle(n):
    fact=1
    for i in range (1,n+1):
        fact*=i
    return fact

fact=Factorielle(n)
print(fact)
        
def binomial(n,p):
    if (0<=p<=n):
        bino=Factorielle(n)//((Factorielle(p)*(Factorielle(n-p))))
        return bino
    else:
        return 0
                             

bino=binomial(n,p)
print(bino)

def maxBinomial(n):
    maxi=1
    for p in range (0,n+1):
       bino
       if bino>maxi:
           maxi=bino
    return maxi
print (maxBinomial(n))

def verifMaxBinomial(n):
    m=n//2
    if( maxBinomial(n)==binomial(n,m)): 
        return True
print (verifMaxBinomial(n))
