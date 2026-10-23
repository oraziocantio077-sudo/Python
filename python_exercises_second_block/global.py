b = 5

def b_funzione():
    global b
    b = 10
    print(b)

print(b)
b_funzione()