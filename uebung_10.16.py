import json
import os

class Produkt:
    def __init__(self, name, preis):
        self.name = name
        self.preis = preis

warenkorb = []

if os.path.exists("warenkorb.json"):
    with open ("warenkorb.json", "r") as datei:
        daten = json.load(datei)
    for x in daten:
        neues_produkt = Produkt(x["name"], x["preis"])
        warenkorb.append(neues_produkt)
    print(f"Produkte im Warenkorb: {neues_produkt.name} = {neues_produkt.preis}€.")
else:
    warenkorb = []

while True:
    print("1: Füge ein neues Produkt dazu")
    print("2: Zeige alle Produkte im Warenkorb")
    print("3: Produkte löschen")
    print("4: Speichern und Beenden")

    wahl = input("Was möchtest du tun? ")

    if wahl == "1":
        name = input("Wie heißt das Produkt? ")
        preis = int(input("Was kostet es? "))
        artikel = Produkt(name, preis)
        warenkorb.append(artikel)
        print(f"{name} wurde hinzugefüht!")

    elif wahl == "2":
        nummer = 1
        print("\n--- WARENKORB ---")
        for i in warenkorb:
            print(f"{nummer}: {i.name} = {i.preis}€.")
            nummer += 1
    
    elif wahl == "3":
        loeschen = int(input("Welches Produkt soll gelöscht werden? Bitte gib die Nummer ein: "))
        index = loeschen - 1
        geloeschter_artikel = warenkorb.pop(index)
        print(f"{geloeschter_artikel.name} wurde gelöscht!")

    elif wahl == "4": 
        liste_fuer_json = []
        for i in warenkorb: 
            produkte_dict = {
                "name": i.name,
                "preis": i.preis,
            }
            liste_fuer_json.append(produkte_dict)
        with open("warenkorb.json", "w") as datei:
            json.dump(liste_fuer_json, datei, indent=4)
        print("Warenkorb erfolgreich gespeichert!")
        break