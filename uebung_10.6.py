import json
import os

neuer_eintrag = {"name": "MontanaBlack", "score": 12000}

if os.path.exists("highscores.json"):
    with open("highscores.json", "r") as datei:
        bestenliste = json.load(datei)
else:
    bestenliste = []

bestenliste.append(neuer_eintrag)

with open("highscores.json", "w") as datei:
    json.dump(bestenliste, datei, indent=4)

print("Highscore erfolgreich hinzugefügt! 🏆")

for x in bestenliste:
    print(f"Auf der Bestenliste sind: {x['name']} mit {x['score']} Punkten!")