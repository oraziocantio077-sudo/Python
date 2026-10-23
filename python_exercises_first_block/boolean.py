age = int(input("Inserire l'eta"))
has_id = False

if (age >= 18):
    has_id = True
    print("Access granted")
else:
    has_id = False
    print("Access denied")