a=int(input("Entrer une annee\n"))
j=int(input("Entrer un jour \n"))
m=int(input("Entrer le chiffre correspondant au mois \n"))
js=0
def kc(j,m,a):
    z=a
    d=j + (23*m//9) + 4 + a + (z//4) - (z//100 ) + (z//400)

    if (m==1 or m==2):
        z=a-1
        js=d%7
    
    else:
        z=a
        js=(d-2)%7
    return js

js=kc(j,m,a)
print("le jour de votre date correspond a",js)

date=[j,m,a]

def jour_semaine (date):
    j=date[0]
    m=date[1]
    a=date[2]
    js=kc(j,m,a)
    if(js==1):
        return "Lundi"
    if(js==2):
        return "Mardi"
    if(js==3):
        return "Mercredi"
    if(js==4):
        return "Jeudi"
    if(js==5):
        return "Vendredi"
    if(js==6):
        return "Samedi"
    if(js==7):
        return "Dimanche"
print (date,"->",jour_semaine (date))

def est_vendredi13(m,a):
    js=kc(13,m,a)
    if(js==5):
        return True
    else:
        return False
print (est_vendredi13(m,a))


