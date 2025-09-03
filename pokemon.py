'''Pokemonspiel
Eine Klasse Pokemon
Jeder Pokemon hat die Eigenschaften Name, Typ, Angriffsstärke, Verteidigungsstärke und Lebenspunkte
Die Verteidigungsstärke wird von der Angriffsstärke abgezogen, die Verbleibende Angriffsstärke von den Lebenspunkten (nicht negativ)
Ein Pokemon mit Lebensstärke = 0 scheidet aus
Die Kämpfe ergeben sich über eine Abfrage
Wenn nur noch ein Pokemon übrig ist, wird dieser als Sieger ausgegeben
'''

from random import randint
class Pokemon:
    def __init__(self, name, angriff, abwehr):
        self.__name = name
        self.__angriff = angriff
        self.__abwehr = abwehr
        self.__schaden = 0
        self.__lebenspunkte = 20
        self.__typ = "Pokemon"
    def get_name(self):
        return self.__name
    def get_angriff(self):
        return self.__angriff
    def get_abwehr(self):
        return self.__abwehr
    def get_lebenspunkte(self):
        return self.__lebenspunkte
    def get_typ(self):
        return self.__typ
    #def schaden(self, angriff, abwehr):
     #   self.__schaden = 0
    #def einstecken(self, schaden):
     #   self.get_lebenspunkte -= schaden
    #def angreifen(self, gegner, schaden):
     #   gegner.einstecken(schaden)
class Wasserpokemon(Pokemon):
    def get_typ(self):
        return "Wasserpokemon"
    def angreifen(self, gegner, schaden):
        print("Wasserangriff")
        return super().angreifen(gegner, schaden)
class Feuerpokemon(Pokemon):
    def get_typ(self):
        return "Feuerpokemon"
    def angreifen(self, gegner, schaden):
        print("Feuerangriff")
        return super().angreifen(gegner, schaden)
class Elektropokemon(Pokemon):
    def get_typ(self):
        return "Elektropokemon"
    def angreifen(self, gegner, schaden):
        print("Elektroangriff")
        return super().angreifen(gegner, schaden)
    #def angreifen(self, gegner, schaden):
     #   return super().angreifen(gegner, schaden)
    #def abwehr(self):
     #   return super().get_abwehr()

pokemonliste = open("pokemon.txt", "r")
print(pokemonliste.read())
abfrage = input("Möchtest du einen neuen Pokemon erstellen? (j/n) ")
def neuer_pokemon():
    pokemon_typ = input("Was für ein Typ ist dein Pokemon? ")
    if pokemon_typ == "Wasser":
        with open("pokemon.txt", "a") as pokemonliste:
                pokemonliste.write("Wasserpokemon, ")
    elif pokemon_typ == "Feuer":
        with open("pokemon.txt", "a") as pokemonliste:
                pokemonliste.write("Feuerpokemon, ")
    elif pokemon_typ == "Elektro":
        with open("pokemon.txt", "a") as pokemonliste:
                pokemonliste.write("Elektropokemon, ")
    else:
        print("Unzulässige Eingabe")
        return
    pokemon_name = input("Wie heißt der neue Pokemon? ")
    with open("pokemon.txt", "a") as pokemonliste:
        pokemonliste.write(pokemon_name)
        pokemonliste.write(", ")
    pokemon_angriff = (input("Wie stark ist dein Pokemon? "))
    with open("pokemon.txt", "a") as pokemonliste:
        pokemonliste.write(pokemon_angriff)
        pokemonliste.write(", ")
    pokemon_abwehr = (input("Wie gut verteidigt dein Pokemon? "))
    with open("pokemon.txt", "a") as pokemonliste:
        pokemonliste.write(pokemon_abwehr)
        pokemonliste.write("\n")    
while abfrage == "j":
    neuer_pokemon()
    abfrage = input("Möchtest du einen neuen Pokemon erstellen? (j/n) ")
print("Die Krieger sind bereit!")
pokemonliste = open("pokemon.txt", "r")
print(pokemonliste.read())


kämpfer = open("pokemon.txt", "r")
pokemon = int(input("Welches Pokemon? "))
a = kämpfer.readlines()[pokemon].split(", ")
print(a)
x, y, z = (a[1]), int(a[2]), int(a[3])
if a[0] == "Wasserpokemon":
     erster_kämpfer = Wasserpokemon(x, y, z)
elif a[0] == "Feuerpokemon":
    erster_kämpfer = Feuerpokemon(x, y, z)
elif a[0] == "Elektropokemon":
    erster_kämpfer = Elektropokemon(x, y, z)
print(erster_kämpfer.get_typ(), erster_kämpfer.get_name(), erster_kämpfer.get_angriff(), erster_kämpfer.get_abwehr())

kämpfer = open("pokemon.txt", "r")
pokemon = int(input("Welches Pokemon? "))
a = kämpfer.readlines()[pokemon].split(", ")
print(a)
x, y, z = (a[1]), int(a[2]), int(a[3])
if a[0] == "Wasserpokemon":
     zweiter_kämpfer = Wasserpokemon(x, y, z)
elif a[0] == "Feuerpokemon":
    zweiter_kämpfer = Feuerpokemon(x, y, z)
elif a[0] == "Elektropokemon":
    zweiter_kämpfer = Elektropokemon(x, y, z)
print(zweiter_kämpfer.get_typ(), zweiter_kämpfer.get_name(), zweiter_kämpfer.get_angriff(), zweiter_kämpfer.get_abwehr())

erster_kämpfer_leben = 20
zweiter_kämpfer_leben = 20
while erster_kämpfer_leben > 0 and zweiter_kämpfer_leben > 0:
    angreifer = randint(0,1)
    if angreifer == 0:
       angreifen = erster_kämpfer.get_angriff()
       abwehr = zweiter_kämpfer.get_abwehr()
       print(erster_kämpfer.get_name(), "greift mit", angreifen, "an")
       print(zweiter_kämpfer.get_name(), "wehrt mit", abwehr, "ab")
       schaden = angreifen - abwehr
       print(erster_kämpfer.get_name(), "verursacht einen Schaden von", schaden)
       zweiter_kämpfer_leben -= schaden
       print(zweiter_kämpfer.get_name(), "hat noch", zweiter_kämpfer_leben, "Lebenspunkte")
    else:
       angreifen = zweiter_kämpfer.get_angriff()
       abwehr = erster_kämpfer.get_abwehr()
       print(zweiter_kämpfer.get_name(), "greift mit", angreifen, "an")
       print(erster_kämpfer.get_name(), "wehrt mit", abwehr, "ab")
       schaden = angreifen - abwehr
       print(zweiter_kämpfer.get_name(), "verursacht einen Schaden von", schaden)
       erster_kämpfer_leben -= schaden
       print(erster_kämpfer.get_name(), "hat noch", erster_kämpfer_leben, "Lebenspunkte")
if erster_kämpfer_leben == 0:
    print(zweiter_kämpfer.get_name(), "hat", erster_kämpfer.get(), "besiegt!")
elif zweiter_kämpfer_leben == 0:
    print(erster_kämpfer.get_name(), "hat", zweiter_kämpfer.get_name(), "besiegt!")
else:
    print("Friede")
