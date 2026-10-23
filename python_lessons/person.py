class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def get_age(self):
        return self.__age
    
    def set_age(self):
        return f"Hai {self.__age} anni? Ne aggiungo 1, ora ne hai {self.__age + 1}"

p1 = Person("Marta", 23)
print(p1.name)
print(p1.get_age())
print(p1.set_age())
#object._classname__privateattribute
print(p1._Person__age) #non lo rende privato, lo maschera (name mangling)
# print(p1.__age)