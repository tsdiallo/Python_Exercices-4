print("suite cyracuse")
n=int(input("Saisissez une valeur\t"))
def f(n):
    if n%2==0:
        return n//2
    else:
        return (3*n)+1
while(True):
    print n,"-->",
    n=f(n)
    if n==1:
        print 1
        break
    
