# a = [1, 2, 3, 2, 3, 4,5 ,6 , 2, 2]

# a.remove(5)
# a.remove(2)
# print(a)

# a = "Forza Catania"

# c = "Catania" in a

# print(c)

# print(a[2:5])

# s = "Hello, World!"
# print(s.capitalize())
# print(s.upper())
# print(s.lower())

# s2 = "     python   "
# print(s2.strip())
# print(s2.replace("th", "TONYPITONY"))

# s = " hello woRLd"
# print(s.strip().capitalize())

# s = "123abc"
# s2 = "123abc-?"

# s3 = "123"
# s4 = "CIAO A TUTTI"


# print(s.isalnum(), s2.isalnum())
# print(s.isdigit(), s3.isdigit())
# print(s.isdigit(), s3.isdigit)
# print(s4.isupper())

# #problemi logici
# age = input("Quanti anni hai mbare?")
# print(age*2) #stampa due volte la stringa non fa il prodotto

#cosi prende in input solo interi

# while (True):
#     age = int(input("Quanti anni hai mbare?"))
#     if(age>0 and age<=99):
#      print(age*2)
#      break
#     else:
#      print("Valore non valido")

# a = int(input("Inserire eta:"))
# if (a<18):
#        print("CBCR")
# elif (a<30):
#        print("Utente giovane")
# elif (a < 60):
#        print("Utente meno giovane")
# else:
#        print("Me nanno")

# is_ad = int(input("Eta':"))


# is_ad = False if a < 18 else True # in una sola riga a differenza di questo:

# if (is_ad < 18):
#      False
# else:
#      True

#fare inserire età all'utente. Se minorenne, stampare "accesso vietato".
# se maggiorenne eseguire un ulteriore controllo. Se età è minore di 35, stampare
# membro junior, se età compresa tra 35 e  50 stampare membro mid
# se età maggiore di 50 stampare membro senior

age = int(input("Inserire età"))

if (age < 18):
     print("accesso vietato")
elif (age>=18 and age <35):
     print("membro junior")
elif (age>=35 and age<50):
     print("membro mid")
elif(age>50):
     print("membro senior")

a = int(input("Inserire età"))

if(a<18):
     print("accesso vietato")
else:
     if (a < 35):
          print("junior")
     elif(a<50):
          print("mid")
     else:
       print("senior")



     
    


