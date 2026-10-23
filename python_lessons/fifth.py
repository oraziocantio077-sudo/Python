a = 0
while a < 5:
    print (a)
    a += 1
else:
    print("Ciclo finito")


a = 0


while a < 11:
    a += 1
    if (a %2 != 0):
        continue
    print(a)
else:
    print("ciclo finito")

fruits = ["fragola", "banana", "cocco"]

# for el in list:

for el in fruits:
    print(el)

for i in range(len(fruits)):
    print(f"elemento {i + 1}: {fruits[i]}")