# Prendiamo uno studente:
# Nome
# Cognome
# Age 
# Corso
# Ciascuno studente deve avere questo schema
# Questo schema prende il nome di classe
# La classe è lo schema che definisce come
# quelle variabili devono essere create
# La classe è come se fosse uno stampino
# La programmazione a oggetti nasce per lavorare
# su variabili specifiche

# Come si usa?
# Incapsulamento
# Consiste nel fatto che i dati non sono liberi
# di viaggiare come variabili globali
# Alcuni pezzi di codice possono accedere alle
# informazioni altri no

class Student:
    # name_p1 = ""
    # role_p1 = "student"
    description = "this class is supposed to be used anytime you will create a new student"
    # class attributes
    name = ""
    def saluta(self):
        print(f"Ciao a tutti, mi chiamo {self.name}")
    

# s1 = Student()

# s1.name = "Tommaso"
# s1.age = 34  #posso assegnare age anche se non è presente come attributo della classe

# s2 = Student()

# s2.name = "Lorenzo"

# print(s1.age)
# print(s1.name, s2.name)
# print(s1.role, s2.role)
# print(s1, s2)

print(Student.description)

s1 = Student()

print(s1.description)

s1.description = "questo alunno è particolarmente sveglio"

print(s1.description) #richiama quello specifico, se assente quello della classe
print(Student.description)

s1.name = "Lorenzo"

s1.saluta()


