numeri = [5, -3, 12, 7, 20, 0, 15, -1]

for n in numeri:
    if n < 0:
        continue  # ignora i negativi

    if n == 0:
        break  # si ferma

    if n >=  10:
        print(n)