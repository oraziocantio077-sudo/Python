username = "admin"
password = ""

if username == "admin" or username == "user" and not password:
    print("Accesso consentito")
else:
    print("Accesso negato")


username = "admin"
password = "1234"

if (username == "admin" or username == "user") and not password:
    print("Accesso consentito")
else:
    print("Accesso negato")