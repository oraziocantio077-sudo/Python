#Esempio 1

# a = []
# for i in range (100):
#     a.append(i*3)
#     print(a)

l = [i*3 for i in range(100)]  # codice meno compatto
print(l)

l = [i*3 for i in range(100) if i < 20]  # codice meno compatto
print(l)

#Esempio 2

a = []
for i in range(20):
    if(i %2 == 0):
        a.append(i)
        print(a)

l = [i for i in range(20) if i %2 == 0]  # codice meno compatto
print(l)

