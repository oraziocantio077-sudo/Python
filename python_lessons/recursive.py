def factorial(n):
    #caso base
    if (n == 0):
        return 1
    else:
        return n*factorial(n-1)
    
a = int(input("Inserisci un numero"))
factorial(a)