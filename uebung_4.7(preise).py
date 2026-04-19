preise = []
einzelpreis = 1
summe = 0

while einzelpreis != 0:
    einzelpreis = float(input("Gib den Preis ein: "))
    if einzelpreis != 0:
        preise.append(einzelpreis)

for x in preise:
    summe = summe + x

print(f"Gesamtsumme: {summe}")