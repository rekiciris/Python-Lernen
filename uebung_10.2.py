import json

with open("produkt_daten.json", "r") as datei:
    geladene_daten = json.load(datei)

print(f"Produktname: {geladene_daten['name']}")
print(f"Preis: {geladene_daten['preis']}")