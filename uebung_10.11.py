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

while True:
    print("\n--- TUNING-WERKSTATT ---")
    print("1: Eine Runde fahren")
    print("2: Auto-Infos anzeigen")
    print("3: Speichern & Beenden")
    
    wahl = input("Was möchtest du tun? (1-3): ")
    
    if wahl == "1":
        km = int(input("Wie viele km willst du fahren? "))
        mein_auto.fahren(km)
        
    elif wahl == "2":
        # DEIN EINSATZ: Gib alle Infos des Autos aus!
        # z.B. "Das Auto ist ein schwarzer BMW mit 10050 km."
        print(f"Das ausgewählte auto ist ein {mein_auto.farbe}er {mein_auto.marke} mit {mein_auto.kilometerstand}km!")
        
    elif wahl == "3":
        # SPEICHERN (Hier kopierst du einfach deinen alten Speicher-Code rein)
        auto_als_dict = {
            "marke": mein_auto.marke,
            "kilometerstand": mein_auto.kilometerstand,
            "farbe": mein_auto.farbe
        }
        with open("auto_speicher.json", "w") as datei:
            json.dump(auto_als_dict, datei, indent=4)
            
        print("Spielstand erfolgreich gespeichert. Tschüss! 👋")
        break # Schleife beenden