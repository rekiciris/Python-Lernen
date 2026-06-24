import json
import os

class Login:
    def __init__(self, webseite, nutzer, passwort):
        self.webseite = webseite
        self.nutzer = nutzer
        self.passwort = passwort

tresor = []

if os.path.exists("safe.json"):
    with open ("safe.json", "r") as datei:
        daten = json.load(datei)
    for x in daten:
        neues_login = Login(x["webseite"], x["nutzer"], x["passwort"])
        tresor.append(neues_login)
    print(f"Daten für Login bei {neues_login.webseite} existiert!")
else:
    tresor = []

while True:
    print("1: Neues Passwort speichern")
    print("2: Alle Logins anzeigen")
    print("3: Login löschen")
    print("4: Speichern und Beenden")

    wahl = input("Was willst du tun? ")

    if wahl == "1":
        webseite = input("Für welche Webseite willst du das Passwort speichern? ")
        nutzer = input("Wie lautet dein Benutzername? ")
        passwort = input("Wie lautet dein Passwort? ")
        daten = Login(webseite, nutzer, passwort)
        tresor.append(daten)
        print(f"Passwort für {webseite} wurde gespeichert!")
    elif wahl == "2":
        nummer = 1
        print("\n--- LOGIN DATEN ---")
        for i in tresor:
            print(f"{nummer}: {i.webseite}: {i.nutzer}, {i.passwort}.")
            nummer += 1
    elif wahl == "3":
        loeschen = int(input("Welches Login soll gelöscht werden? Bitte gib die Nummer ein: "))
        index = loeschen - 1
        geloeschter_login = tresor.pop(index)
        print(f"Login für {geloeschter_login.webseite} wurde gelöscht!")
    elif wahl == "4":
        liste_fuer_json = []
        for i in tresor: 
            login_dict = {
                "webseite": i.webseite,
                "nutzer": i.nutzer,
                "passwort": i.passwort,
            }
            liste_fuer_json.append(login_dict)
        with open("safe.json", "w") as datei:
            json.dump(liste_fuer_json, datei, indent=4)
        print("Logins erfolgreich gespeichert!")
        break