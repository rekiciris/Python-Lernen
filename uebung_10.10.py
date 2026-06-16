import json
import os

class Auto:
    def __init__(self, marke, kilometerstand, farbe):
        self.marke = marke
        self.kilometerstand = kilometerstand
        self.farbe = farbe
    def fahren(self, km):
        self.kilometerstand += km
        print(f"Der {self.farbe}e {self.marke} ist {km} km gefahren. Gesamt: {self.kilometerstand} km")

if os.path.exists("auto_speicher.json"):
    with open("auto_speicher.json", "r") as datei:
        daten = json.load(datei)

    mein_auto = Auto(daten["marke"], daten["kilometerstand"], daten["farbe"])
    print(f"--- Auto erfolgreich geladen! Start-KM: {mein_auto.kilometerstand} ---")
else:
    mein_auto = Auto("BMW", 10000, "schwarz")
    print("--- Neues Auto erstellt! ---")

mein_auto.fahren(50)

auto_als_dict = {
    "marke": mein_auto.marke,
    "kilometerstand": mein_auto.kilometerstand,
    "farbe": mein_auto.farbe
}

with open("auto_speicher.json", "w") as datei:
    json.dump(auto_als_dict, datei, indent=4)