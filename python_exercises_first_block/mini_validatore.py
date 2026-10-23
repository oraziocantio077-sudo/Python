a = input("Inserisci il tuo username\n")

b = input("Inserisci la tua password\n")

if (a.strip() == "" and len(b) < 6):
    print("Invalid")
else:
     print("Valid")




