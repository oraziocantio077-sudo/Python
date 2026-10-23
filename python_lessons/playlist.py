#INTROSPECTION E REFLECTION
# print(type(pl1))
# print(isinstance(pl1, Playlist))
#print("Has promotion?", hasattr(pl1 "title"))
#print(list(pl1.__dict__))

# a = input("Inserisci l'attributo da cercare")
# print(f"risultato {hasattr(pl1, a)}")

# print(pl1.name) HARDCODED

# a = input("Inserisci attributo a cui sei interessato")

# if hasattr(pl1, a):
    #print(getattr(pl1, a, "attributo non trovato")) SOFT CODED
#   else:
#     b = input("Attributo non trovato, inserire adesso il valore che si vuole associare")
#     setattr(pl1, a, b)

# print(getattr(pl1, a))





class Playlist:
    description = "class used to represent playlists"

    def __init__ (self, name, pl_descr, songs= []):
        self.name = name
        self.pl_descr = pl_descr
        self.songs = songs

    def __add__(self, other):
        if isinstance(other, Playlist):
            nuovo_nome = self.name + " + " + other.name
            nuova_pldescr = f"Playlist creata automaticamente unendo {self.name} e {other.name}"
            nuove_songs = self.songs + other.songs

            return Playlist(nuovo_nome, nuova_pldescr, nuove_songs)

        else:
            print("Non posso sommare gli elementi chiesti")
            return 

    def __str__(self):
        a = f'''Titolo della playlist {self.name}\n
             {self.pl_descr}\n
             questa playlist contiene esattamente {len(self.songs)} canzoni\n
             '''
        return a

    
pl1 = Playlist("Estate 25", "Le canzoni di quando ho conosciuto Morena", ['maracaibo', 'danza kuduro'])
pl2 = Playlist("Estate 24", "Le canzoni di quando ho conosciuto Alessia", ['macarena', 'volare', 'buoni o cattivi'])

pl3 = pl1 + pl2

print(pl3.name)
print(pl3.pl_descr)
print(pl3.songs)
