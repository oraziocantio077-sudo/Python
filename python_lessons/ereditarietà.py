# class Vehicle:
#     def __init__(self, model, year):
#         self.model = model
#         self.year = year
    
#     def accelerate(self):
#         print(f"{self.model} sta accelerando")
    
#     def sterzo(self, angolo):
#         print(f"{self.model} sta sterzando di {angolo} gradi")

# class Car(Vehicle):
#     def __init__(self, model, year, doors = 5):
#         super().__init__(model, year)
#         self.doors = doors

# class Motorcycle(Vehicle):
#     def __init__(self, model, year, cambio = "manuale"):
#         super().__init__(model, year)
#         self.cambio = cambio

# c1 = Car("Fiat", 2012, 7)
# c2 = Car("BMW", 2023)

# c1.accelerate()
# c2.sterzo(25)  #eredita i metodi di Vehicle e ogni classe estende di base la classe Object

#OVERRIDE
class Vehicle:
    def __init__(self, model, year):
        self.model = model
        self.year = year
    
    def accelerate(self):
        print(f"{self.model} sta accelerando")
    
class Car(Vehicle):
    def __init__(self, model, year, doors = 5):
        super().__init__(model, year)
        self.doors = doors
    def accelerate(self):
        print(f"{self.model} sta acceleando, ti ricordo che è una car a {self.doors} porte")
    def ex_accelerate(self):
        super().accelerate()


c1 = Car("mazda", 2002)

c1.accelerate()
c1.ex_accelerate()