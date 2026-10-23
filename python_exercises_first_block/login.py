username = "admin"
inserted_username = input("Inserire l'username\n")
password = input("Inserire la password\n")


if (inserted_username == username and password.strip()):
    print("Login OK")
else:
    print("Login failed")
