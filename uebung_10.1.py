import json

produkt = {"name": "Gaming Monitor", "preis": 299.99, "verfuegbar": True}

with open("produkt_daten.json", "w") as datei:
    json.dump(produkt, datei, indent=4)

print("JSON-Datei wurde erfolgreich gespeichert!")