a = int(input("Inserisci un voto\n"))

if (a < 60):
    print("Fail")
elif (a > 60 and a <= 79):
    print("Pass")
else:
    print("Excellent")