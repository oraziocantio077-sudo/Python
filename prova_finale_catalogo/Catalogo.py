class Libro:
    def __init__(self, titolo, autore, casa_editrice, prezzo_acquisto):
        self.titolo = titolo
        self.autore = autore
        self.casa_editrice = casa_editrice
        self.__prezzo_acquisto = prezzo_acquisto 

    
    def get_prezzo(self):
        return self.__prezzo_acquisto
    
    def set_prezzo(self, nuovo_prezzo):
        if nuovo_prezzo >= 0:
            self.__prezzo_acquisto = nuovo_prezzo 
        else:
            print("Il prezzo non può essere negativo")

class Catalogo:
    def __init__(self, nome, descrizione):
        self.nome = nome
        self.descrizione = descrizione
        self.lista_libri = [] 
        self.__valore_totale = 0.0

    
    def get_valore_totale(self):
        return self.__valore_totale

    
    def __ricalcola_valore(self):
        self.__valore_totale = sum(libro.get_prezzo() for libro in self.lista_libri)

    
    def aggiungi_libro(self, libro):
        if isinstance(libro, Libro):
            self.lista_libri.append(libro)
            self.__ricalcola_valore()
        else:
            print("Puoi aggiungere solo oggetti della classe Libro")

    def rimuovi_libro(self, libro):
        if libro in self.lista_libri:
            self.lista_libri.remove(libro)
            self.__ricalcola_valore()
        else:
            print("Libro non trovato nel catalogo")

    
    def __eq__(self, other):
        if not isinstance(other, Catalogo):
            return False
        
        return (self.nome == other.nome and 
                self.descrizione == other.descrizione and 
                self.lista_libri == other.lista_libri)

    
    def __add__(self, other):
        if not isinstance(other, Catalogo):
            raise TypeError("Puoi sommare solo due oggetti Catalogo")
        
        
        nuovo_nome = f"{self.nome} + {other.nome}"
        nuova_desc = f"Unione di {self.nome} e {other.descrizione}"
        nuovo_catalogo = Catalogo(nuovo_nome, nuova_desc)
        
        
        for libro in self.lista_libri + other.lista_libri:
            nuovo_catalogo.aggiungi_libro(libro)
            
        return nuovo_catalogo


l1 = Libro("Il Signore degli Anelli", "J.R.R. Tolkien", "Bompiani", 25.0)
l2 = Libro("1984", "George Orwell", "Mondadori", 12.5)
l3 = Libro("Il Nome della Rosa", "Umberto Eco", "Bompiani", 18.0)

cat_fantasy = Catalogo("Fantasy", "Libri di genere fantasy")
cat_classici = Catalogo("Classici", "Grandi classici della letteratura")

cat_fantasy.aggiungi_libro(l1)
cat_classici.aggiungi_libro(l2)
cat_classici.aggiungi_libro(l3)

print(f"Valore catalogo Fantasy: {cat_fantasy.get_valore_totale()}€") 
print(f"Valore catalogo Classici: {cat_classici.get_valore_totale()}€")

cat_totale = cat_fantasy + cat_classici
print(f"\nNome nuovo catalogo: {cat_totale.nome}")
print(f"Valore totale unito: {cat_totale.get_valore_totale()}€")

cat_totale.rimuovi_libro(l2)
print(f"Valore dopo aver rimosso '1984': {cat_totale.get_valore_totale()}€")

cat_copia = Catalogo("Fantasy", "Libri di genere fantasy")
cat_copia.aggiungi_libro(l1)
print(f"\nIl catalogo Fantasy è uguale alla sua copia? {cat_fantasy == cat_copia}")

