import json

class Spieler:
    def __init__(self, name, level, klasse):
        self.name = name
        self.level = level
        self.klasse = klasse
    def profil_speichern(self):
        daten = {"name": self.name, "level": self.level, "klasse": self.klasse}
        with open("spieler_profil.json", "w") as datei:
            json.dump(daten, datei, indent=4)
        print("Profil gespeichert!")

def profil_laden():
    with open("spieler_profil.json", "r") as datei:
        geladene_daten = json.load(datei)
    
        neuer_held = Spieler(
        name=geladene_daten["name"],
        level=geladene_daten["level"],
        klasse=geladene_daten["klasse"]
    )
    return neuer_held

mein_held = profil_laden()

print(f"Erfolgreich geladen: {mein_held.name} (Level {mein_held.level}) ist ein stolzer {mein_held.klasse}!")