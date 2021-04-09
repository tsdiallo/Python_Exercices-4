def fonction_C2F():
    C=float(input("Entrer votre temperature\t"))
    f=C*1.8+32
    return round(f)

f=fonction_C2F()
print("votre temperature en fahrenheit fait\t",f)
