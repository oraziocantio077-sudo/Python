def saluto(nome):
    print(f"Ciao {nome}!")

def moltiplicazione(a , b = 5): # i parametri di default sempre alla fine
    if a == 3:
        return 3
    else:
        print(a*b)


print("Qua inizia il programma")
saluto("Orazio")
moltiplicazione(3,4)
moltiplicazione("Franco", 3)
print(moltiplicazione(3,4)) # 3 e 4 sono gli argomenti
print(moltiplicazione(4))  