def bissextile(a):
    annee=False
    if a%4==0 and a%100!=0 or a%400==0:
        annee=True
    return annee

a=int(input("Entrer une annee\t"))
print(bissextile(a))
