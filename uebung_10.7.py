import json
import os

neuer_artikel = {"artikel": "Bananen", "anzahl": 5}

if os.path.exists("einkauf.json"):
    with open("einkauf.json", "r") as datei:
        einkaufsliste = json.load(datei)
else:
    einkaufsliste = []

einkaufsliste.append(neuer_artikel)

with open("einkauf.json", "w") as datei:
    json.dump(einkaufsliste, datei, indent=4)

print("Artikel hunzugefügt! \n")

print("--- DEIN EEINKAUFSZETTEL ---")

for x in einkaufsliste:
    print(f"{x['anzahl']} - {x['artikel']}")