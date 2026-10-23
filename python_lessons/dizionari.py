# a = ["GM", 27, "M"]

# print(a[0], a[1], a[2])

d = {'name': 'Gianmarco', 'age': 27, 'gender': 'M'}
print(type(d))
print(d)

a = input("Dimmi che vuoi sapere di sto tipo")

print(d.get(a, 'chiave non esistente')) #codice molto più dinamico

if ('age' in d):
    print(d['age'])

print(len(d))

print(sorted(d))
    
d.pop('gender')

print(d)

d.popitem()

print(d)

d.clear()

print(d)

for key in d.keys():
    print(key, d[key])

