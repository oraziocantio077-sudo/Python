name = "Emanuele"
age = 52
is_funny = True

print(type(name), type(age), type(is_funny))

a = [1, 5.4, False, "Pietro", [1,2,3]]
print(a)

a = [["Gianmarco", 27], ["Mirko", 36], ["Luca", 20], ["Orazio"]]
print(a[3])
print(a[3][0])

#tuple

b=("Ciccio", 0, 1, False)
print(b[0])

#La tupla è immutabile

#convertire la tupla in lista

print(type(b))

c = list(b)

print(type(c))


frutti = ["ananas", "mela", "banana", "arancia"]
print(frutti)

frutti.append("pera")

print(len(frutti))

a = frutti.pop()

frutti.pop()

print(a)

print(frutti)

b = frutti.pop(2)
print(frutti)

