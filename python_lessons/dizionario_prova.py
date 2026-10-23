d = {'name': 'Orazio', 'age': 19, 'gender': 'M'}
print(d['name'])
print(f"Ciao mi chiamo {d['name']}")
a = input("Dimmi cosa vuoi sapere di sto soggetto\n")
print(d.get(a, 'informazione non disponibile'))
d.pop('name')
print(d)