correct_password = "123abc"
tentativi = 0


while (True):
    password = input("Inserisci la password\n")

    password = password.strip().lower()

    if (password == correct_password):
        print("Accesso effettuato")

        break
        
        
    elif (password != correct_password):
        print("Password errata\n")
        tentativi += 1
        if(tentativi>=3):
            print("Riprova più tardi, Forza Palermo\n")
            break