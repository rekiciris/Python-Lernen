import json
import os

class Aufgabe:
    def __init__(self, titel, prio, stunden):
        self.titel = titel
        self.prio = prio
        self.stunden = stunden

projekt_aufgaben = []

if os.path.exists("aufgaben.json"):
    with open ("aufgaben.json", "r") as datei:
        daten = json.load(datei)
    for x in daten:
        neue_aufgabe = Aufgabe(x["titel"], x["prio"], x["stunden"])
        projekt_aufgaben.append(neue_aufgabe)
    print(f"Die Aufgabe {x.titel}, priorität {x.prio}, dauert {x.stunden} Stunden.")
else:
    projekt_aufgaben = []

while True:
    print("1: Hinzufügen")
    print("2: Aufgaben anzeigen")
    print("3: Aufgabe löschen")
    print("4: Speichern & Beenden")

    wahl = input("Was möchtest du tun? (1-4) ")

    if wahl == "1":
        titel = input("Wie heißt die Aufgabe? ")
        prio = input("Welche priorität hat die Aufgabe? ")
        stunden = int(input("Wie lange dauert die Aufgabe? "))
        projekt = Aufgabe(titel, prio, stunden)
        projekt_aufgaben.append(projekt)
        print(f"Aufgabe {titel} wurde erstellt!")

    elif wahl == "2":
        nummer = 1
        print("\n--- DEINE AUFGABEN ---")
        for i in projekt_aufgaben:
            print(f"{nummer}: {i.titel} (Prio: {i.prio}) - {i.stunden} Std.")
            nummer += 1

    elif wahl == "3":
        loeschen = int(input("Welche Aufgabe soll gelöscht werden? Bitte gib die Nummer ein."))
        index = loeschen - 1
        geloeschte_aufgabe = projekt_aufgaben.pop(index)
        print(f"Aufgabe {geloeschte_aufgabe.titel} wurde gelöscht!")
        
    elif wahl == "4": 
        liste_fuer_json = []
        for i in projekt_aufgaben: 
            aufgaben_dict = {
                "titel": i.titel,
                "prio": i.prio,
                "stunden": i.stunden
            }
            liste_fuer_json.append(aufgaben_dict)
        with open("aufgaben.json", "w") as datei:
            json.dump(liste_fuer_json, datei, indent=4)
        print("Aufgaben erfolgreich gespeichert!")
        break