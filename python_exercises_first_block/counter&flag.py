a = int(input("Si prega di inserire un numero (Inserire 0 per uscire)\n"))
counter_positivi = 0
continua = True

while (continua == True):
    if a > 0:
        counter_positivi += 1
        continua = True
        
    elif a == 0:
        continua = False

print(f"I numeri positivi inseriti sono {counter_positivi}")
