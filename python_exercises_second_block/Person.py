class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Ciao {self.name}" 

p1 = Person("Orazio", 19)
print(p1.greet())
