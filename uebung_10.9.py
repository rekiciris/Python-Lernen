import json
import os

# 1. Wir definieren die Klasse wie gewohnt
class Auto:
    def __init__(self, marke, kilometerstand):
        self.marke = marke
        self.kilometerstand = kilometerstand
        
    def fahren(self, km):
        self.kilometerstand += km
        print(f"Der {self.marke} ist {km} km gefahren. Gesamt: {self.kilometerstand} km")

# 2. LADEN: Gibt es die Datei schon?
if os.path.exists("auto_speicher.json"):
    with open("auto_speicher.json", "r") as datei:
        daten = json.load(datei)
    
    # JETZT DER TRICK: Wir bauen aus den geladenen Dictionary-Daten wieder ein ECHTES Objekt!
    mein_auto = Auto(daten["marke"], daten["kilometerstand"])
    print(f"--- Auto erfolgreich geladen! Start-KM: {mein_auto.kilometerstand} ---")
else:
    # Falls keine Datei existiert, erstellen wir ein brandneues Auto
    mein_auto = Auto("BMW", 10000)
    print("--- Neues Auto erstellt! ---")

# 3. DAS AUTO FÄHRT
# Jedes Mal, wenn du das Programm startest, fährt das Auto 50 km weiter!
mein_auto.fahren(50)

# 4. SPEICHERN: Wir verwandeln das Objekt in ein Dictionary
auto_als_dict = {
    "marke": mein_auto.marke,
    "kilometerstand": mein_auto.kilometerstand
}

with open("auto_speicher.json", "w") as datei:
    json.dump(auto_als_dict, datei, indent=4)