try:
    a = int(input("Inserisci un numero\n")) #potrebbe verificarsi un value error

    b = 5 / a #ZeroDivisionError

    print(b)

# except (ValueError, ZeroDivisionError) as e:
#     print(f"errore {e}, {type(e)}")
#     print(f"errore {str(e)}, {repr(e)}")
except ZeroDivisionError as e:
    print("Non puoi dividere per 0, capra.")
    raise ZeroDivisionError("te lo avevo detto capra")
except:
    print("Errore generico")

else: #si attiva solo se il try va a buon fine
    print("andato a buon fine")
finally:
    print("Questo si attiva in ogni caso")
