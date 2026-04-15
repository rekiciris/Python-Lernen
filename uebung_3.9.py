getraenke_preise = [3.50, 6.20, 2.80, 5.50, 4.00, 7.50]
total = 0
teure_drinks = 0

for x in getraenke_preise:
    total = total + x
    if x > 5:
        teure_drinks = teure_drinks + 1

print(f"Gesamtrechnung: {total} Euro.")
print(f"Anzahl der teuren Drinks: {teure_drinks}")