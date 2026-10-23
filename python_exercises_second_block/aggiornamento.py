car = {"brand": "Toyota", "year": 2020}

car.update({"price": 2000, "year": 2022})

a = input("Inserisci\n")

print(car.get(a, "chiave non esistente"))