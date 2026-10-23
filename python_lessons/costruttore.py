class Student:
    description = "this class bla bla"
    #class attributes

    def __init__(self, name, surname, age, course):
        self.name = name.strip().capitalize()
        self.surname = surname.strip().capitalize()
        self.age = age
        self.course = course
        self.fullname = self.name + " " + self.surname
        # INSTANCE ATTRIBUTES

    def __eq__(self, other):
        if isinstance(other, Student): #va a controllare se è un oggetto dell'istanza Student
            if(self.name == other.name and self.surname == other.surname and self.age == other.age):
                return True
            else:
                return False
        else:
            return False
        
    

s1 = Student("Salvatore", "Pappalardo", 15, "web developer")
s2 = Student("Salvatore", "Pappalardo", 40, "web developer")
s3 = Student("Salvatore", "Pappalardo", 15, "cybersecurity")

print(s1 == s2) #False
print(s1 == s3) #True

