a = input("Inserire una stringa (scrivere stop per terminare)\n")

continua = True

while continua:
    if a == "stop":
        continua = False
        print("Uscita dal programma")
    else:
        a = input("Inserire un altra stringa\n")