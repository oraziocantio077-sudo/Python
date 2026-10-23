def prodotto(*numeri): #Args: prende tutti i parametri e li salva dentro
                        # una tupla
    a = 1
    for el in numeri:
        a*= el
    return a

def team(**amesquatra): 
    # Kwargs: Gestisce un numero variabile di argomenti nominati (chiave-valore).
    print("Vi presento a me squatra")
    print("ruoli previsti:", amesquatra.keys())
    print("ve la presento meglio:")
    for role, name in amesquatra.items():
        print(role, name)


print(prodotto(5))
print(prodotto(4,5))
print(prodotto(3,2,7))
team(founder = "Gianmarco", Cofounder = "Francesco", ambassador = "Mirko")

