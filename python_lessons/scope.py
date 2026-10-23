def saluto(nome):
    print(f"ciao, {nome}")
    b = 5   # b esiste solo qua dentro, è una 
            # variabile locale

saluto("Giacomo")

def saluto(nome):
    global b
    print(f"ciao, {nome}")
    b = 343
    print(b)   
            
b = 5
saluto("Giacomo") #in questo caso invocando la funzione b prenderà
print (b)         # il valore dentro la funzione (343), successivamente
                  # infine b prendere il valore assegnato fuori (5)