# class Vehicle:
#     def accelerate(self):
#         print("Il veicolo sta accelerando")

# class Car:
#     def accelerate(self):
#         print("La macchina sta accelerando")

# class SuperCar(Vehicle, Car): #Polimorfismo, prende la prima classe passata nel costruttore 
#     color = "red"

# pandino = SuperCar()
# pandino.accelerate()


#dynamic dispactch
class Car:
    def accelerate(self):
        print("La macchina accelera col pedale")

class Moto:
    def accelerate(self):
        print("La moto accelera con la manopola")

class Bici:
    def accelerate(self):
        print("La bici accelera spingendo")

lista = []

c1 = Car()

lista.append(c1)

m1 = Moto()

lista.append(m1)

b1 = Bici()

lista.append(b1)

print(lista)

for el in lista:
    el.accelerate()