a=["sa", "1984", "hp"]
b=["eragon", "3ms", "hp"]

c = []

for el in a+b:
    if el not in c:
        c.append(el)

print(c)