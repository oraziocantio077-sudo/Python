def fattoriale(n):
    if n == 0 or n == 1:   
        return 1
    else:
        return n * fattoriale(n - 1)

print(fattoriale(5))