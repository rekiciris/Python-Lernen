import json
import os

class Mitarbeiter:
    def __init__(self, name, job, gehalt):
        self.name = name
        self.job = job
        self.gehalt = gehalt

belegschaft = []

if os.path.exists("mitarbeiter.json"):
    with open ("mitarbeiter.json", "r") as datei:
        daten = json.load(datei)
    for x in daten:
        arbeiter = Mitarbeiter(x["name"], x["job"], x["gehalt"])
        belegschaft.append(arbeiter)
    print(f"Mitarbeiter {x.name} ({x.job}) verdient {x.gehalt}€.")
else:
    belegschaft = []
    print("Du hast noch keine MItarbeiter!")

while True:
    name = input("Wie heißt der Mitarbeiter? ")
    job = input("Als was arbeitet sie/er? ")
    gehalt = int(input("Wie viel verdient sie/er? "))
    neuer_arbeiter = Mitarbeiter(name, job, gehalt)
    belegschaft.append(neuer_arbeiter)
    print(f"{name} wurde erfolgreich eingestellt!\n")

    print("1: Weitern Mitarbeiter anlegen")
    print("2: Speichern und Beenden")
    entscheidung = input("Was möchtest du tun? 1 oder 2? ")
    if entscheidung == "2":
        liste_fuer_json = []
        for i in belegschaft: 
            mitabeiter_dict = {
                "name": i.name,
                "job": i.job,
                "gehalt": i.gehalt
            }
            liste_fuer_json.append(mitabeiter_dict)
        with open("mitarbeiter.json", "w") as datei:
            json.dump(liste_fuer_json, datei, indent=4)
        print("Mitarbeiterverzeichnis erfolgreich gespeichert!")
        break