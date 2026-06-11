import json
import os

# Ein neuer Spieler, den wir hinzufügen wollen
neuer_eintrag = {"name": "MontanaBlack", "score": 12000}

# 1. PRÜFEN: Gibt es die Datei überhaupt schon?
# Wenn ja, laden wir die alte Liste. Wenn nein, starten wir mit einer leeren Liste.
if os.path.exists("highscores.json"):
    with open("highscores.json", "r") as datei:
        bestenliste = json.load(datei)
else:
    bestenliste = [] # Leere Liste, falls das Spiel zum ersten Mal startet

# 2. HINZUFÜGEN: Wir hängen den neuen Eintrag an die Liste an
bestenliste.append(neuer_eintrag)

# 3. SPEICHERN: Die aktualisierte Liste wird wieder weggeschrieben
with open("highscores.json", "w") as datei:
    json.dump(bestenliste, datei, indent=4)

print("Highscore erfolgreich hinzugefügt! 🏆")