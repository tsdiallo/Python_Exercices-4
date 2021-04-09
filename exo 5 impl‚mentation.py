def max(a,b):
    if a>b:
        maxi=a
    else:
        maxi=b
    return maxi

a=int(input("Entrer un chiffre\t"))
b=int(input("Entrer un chiffre\t"))

maxi=max(a,b)
print("le max des deux nombres est",maxi)
