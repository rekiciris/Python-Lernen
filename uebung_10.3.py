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

held1 = Spieler("Geonkh", 42, "Magier")
held1.profil_speichern()