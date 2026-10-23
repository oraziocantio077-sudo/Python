command = input("Inserisci un comando")

match command:
    case "start":
        print("Il programma sta iniziando")
    case "stop":
        print("Il programma sta finendo")
    case "help":
        print("FORZA CATANIA")
    case _:
        print("FORZA PALERMO")