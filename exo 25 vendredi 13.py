def lendemain(js,j,m,a):
    mois30 = [4, 6, 9, 11]
    mois31 = [1, 3, 5, 7, 8, 10]
    demain= 1 + (js % 7)
  
    if (m==12 and j==31 ):
        demain=demain
        j=1
        m=1
        a=a+1
        return [demain,j,m,a]

    elif((j==30 and m in mois30) or (j==31 and m in mois31) or(j==29 and m==2) or (j==28 and m==2 and  not(a%400==0 or (a%4==0 and a%100!=0)))):
        demain=demain
        j=1
        m=m+1
        a=a
        
        return [demain,j,m,a]
    else:
        demain=demain
        j=j+1
        m=m
        a=a
        return [demain,j,m,a]
print (2, 8, 12, 2015),"->",lendemain (2, 8, 12, 2015)
print (5, 1, 1, 2016),"->",lendemain (5, 1, 1, 2016)
print(4, 31, 12, 2015), "->",lendemain (4, 31, 12, 2015)
print (7, 31, 1, 2016),"->",lendemain (7, 31, 1, 2016)
print (6, 30, 1, 2016),"->",lendemain (6, 30, 1, 2016)
print (1, 29, 2, 2016),"->",lendemain (1, 29, 2, 2016)
print (7, 28, 2, 2016),"->",lendemain (7, 28, 2, 2016)
print (6, 28, 2, 2015),"->",lendemain (6, 28, 2, 2015)
print (6, 16, 7, 2016),"->",lendemain (6, 16, 7, 2016)
print"***************************************************"
print "Aujourd'hui c'est le jeudi 11 Novembre 2017"
print"les 10 vendredis 13 prochains sont:"
js=4
j=9
m=11
a=2017

cpt=0

while (cpt<10):
    date=lendemain(js, j,m,a)
    js=date[0]
    j=date[1]
    m=date[2]
    a=date[3]
    
    if (js==5 and j==13):
        
        print "vendredi 13/",m,"/",a
        cpt=cpt+1
       
          
