# Funzione Split

s = "Ciao a tutti oggi è una giornata meravigliosa"

s2 = s.split()

print(s2)

lw = [len(i) for i in s2] #per ciascuna parola ne calcolo la lunghezza

cw = [i.capitalize() for i in s2]

ow = ["p" if len(i) % 2 == 0 else "d" for i in s2 if i.isalpha()]

print(lw)

print(cw)

print(ow)

