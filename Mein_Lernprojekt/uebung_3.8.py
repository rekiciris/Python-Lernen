noten = [1, 3, 2, 5, 4, 2]
summe = 0
bestanden = 0

for x in noten:
    summe = summe + x
    if x <= 4:
        bestanden = bestanden + 1
durchschnitt = summe / 6

print(f"Durchscnittsnote: {durchschnitt}")
print(f"Anzahl der Schüler, die bestanden haben: {bestanden}")