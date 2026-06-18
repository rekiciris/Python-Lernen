import json
import os

class Sparschwein:
    def __init__(self, kontostand):
        self.kontostand = kontostand
    def einzahlen(self, betrag):
        self.betrag = betrag
        self.kontostand = betrag + self.kontostand

if os.path.exists("sparschwein.json"):
    with open ("sparschwein.jon", "r") as datei:
        daten = json.load(datei)
    mein_schwein = Sparschwein(daten["kontostand"])
    print(f"Der Kontostand deines Sparschweines ist {mein_schwein.kontostand}€.")
else:
    mein_schwein = Sparschwein(0)
    print("Dein Sparschwein wurde eröffnet!")

while True:
    print("\n--- SPARSCHWEIN ---")
    print("1: Einzahlen!")
    print("2: Kontostand anzeigen")
    print("3: Speichern & Beenden")
    
    wahl = input("Was möchtest du tun? (1-3): ")
    
    if wahl == "1":
        euro = int(input("Wie viel Geld willst su einzahlen? "))
        mein_schwein.einzahlen(euro)
        print(f"Du hast {mein_schwein.betrag}€ eingezahlt! Der Kontostand ist {mein_schwein.kontostand}€.")
        
    elif wahl == "2":
        print(f"Der Kontostand deines Sparschweines ist {mein_schwein.kontostand}€.")
        
    elif wahl == "3":
        sparschwein_als_dict = {
            "kontostand": mein_schwein.kontostand,
        }
        with open("sparschwein_speicher.json", "w") as datei:
            json.dump(sparschwein_als_dict, datei, indent=4)
            print("Aus dem Sparschwein-Konto Ausgelogt. Tschüss! 👋")