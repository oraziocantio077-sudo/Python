def somma(n):
    if n == 0:
        return 0
    else:
        return n + somma(n - 1)

print(somma(5))