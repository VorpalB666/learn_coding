'''Login
Abfrage ober Login oder neuen Account anlegen
Möglichkeit, neue Daten anzulegen
Abfrage von Nutzername und Passwort
Abgleich der eingegebenen Daten mit den gespeicherten Daten
Möglichkeit, Passwort zu ändern
Empfehlungen für ein sicheres Passwort
Passwortgenerator
'''
import random

def einstieg():
    abfrage = input("Login (L), neuen Account (A), Passwort ändern (C), Account löschen (D)? ")
    if abfrage == ("L"):
        login()
    elif abfrage == ("A"):
        neuer_account()
    elif abfrage == ("C"):
        passwort_ändern()
    elif abfrage == ("D"):
        account_löschen()
    else:
        print("Fehlerhafte Eingabe")
        einstieg()
        
def neuer_account():
    benutzername = input("Benutzername: ")
    zufall_frage = input("Möchten Sie ein Zufallspasswort erstellen lassen? (J) ")
    if zufall_frage == "J":
        passwort = zufallspasswort()
    else:
        passwort = passwort_eingeabe()
    print("Benutzername: ", benutzername, "Passwort: ", passwort)
    neuer_nutzer = benutzername, passwort
    with open("zugangsdaten.txt", "a+") as zugangsdatenliste:
        zugangsdatenliste.write("\n"+ str(neuer_nutzer))

def passwort_eingeabe():
    passwort = input("Passwort: ")
    if len(passwort) < 8:
        print("Das Passwort muss mindestens 8 Zeichen lang sein")
        passwort_eingeabe()
    Sonderzeichen = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "+", "§"]
    if not any(char in Sonderzeichen for char in passwort):
        print("Das Passwort muss mindestens ein Sonderzeichen enthalten")
        passwort_eingeabe()
    if not any(char.isupper() for char in passwort):
        print("Das Passwort muss mindestens einen Großbuchstaben enthalten")
        passwort_eingeabe()
    if not any(char.islower() for char in passwort):
        print("Das Passwort muss mindestens einen Kleinbuchstaben enthalten")
        passwort_eingeabe()
    if not any(char.isdigit() for char in passwort):
        print("Das Passwort muss mindestens eine Zahl enthalten (!@#$%^&*()-+§)")
        passwort_eingeabe()
    else:
        return passwort

def zufallspasswort():
    zeichen = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-+"
    passwort = "".join(random.sample(zeichen, 12))
    return passwort

def login():
    username = input("Benutzername: ")
    with open("zugangsdaten.txt", "r") as zugangsdatenliste:
        zugangsdaten = {key.strip("('"): value.strip("')").strip("\n").strip(")\n").strip(" '") for key, value in (line.split(',', 1) for line in zugangsdatenliste)}
        schloss = zugangsdaten.get(username)
    for benutzer in zugangsdaten:
        if benutzer == username:
            passwort_abfrage(schloss)
            return schloss
    else:
        print("Benutzer nicht bekannt")
        login()

def passwort_abfrage(schloss):
    a = 0
    while a < 4:
        password = input("Passwort: ")
        if password == schloss:
            print("Sesam öffne dich")
            break
        else:
            print("Falsches Passwort")
            a += 1
    if a == 4:
        print("Schleich di!")
        exit()

def passwort_ändern():
    username = input("Benutzername: ")
    with open("zugangsdaten.txt", "r") as zugangsdatenliste:
        zugangsdaten = {key.strip("('"): value.strip("')").strip("\n").strip(")\n").strip(" '") for key, value in (line.split(',', 1) for line in zugangsdatenliste)}
        schloss = zugangsdaten.get(username)
    altes_passwort = input("Altes Passwort: ")
    if altes_passwort == schloss:
        neues_passwort = passwort_eingeabe()
        zugangsdaten[username] = neues_passwort
        with open("zugangsdaten.txt", "w") as zugangsdatenliste:
            for key, value in zugangsdaten.items():
                zugangsdatenliste.write(f"{key}, {value}\n")
        print("Benutzername: ", username, "Neues Passwort: ", neues_passwort)
    else:
        print("Falsches Passwort")
        passwort_ändern()

def account_löschen():
    username = input("Benutzername: ")
    with open("zugangsdaten.txt", "r") as zugangsdatenliste:
        zugangsdaten = {key.strip("('"): value.strip("')").strip("\n").strip(")\n").strip(" '") for key, value in (line.split(',', 1) for line in zugangsdatenliste)}
        schloss = zugangsdaten.get(username)
    passwort = input("Passwort: ")
    if passwort == schloss:
        del zugangsdaten[username]
        with open("zugangsdaten.txt", "w") as zugangsdatenliste:
            for key, value in zugangsdaten.items():
                zugangsdatenliste.write(f"{key}, {value}\n")
        print("Account gelöscht")

einstieg()
