preise = [12.50, 30.0, 45.0, 9.99, 21.0]
summe = 0
for x in preise:
    summe = summe + x
    print(f"Artikel hinzugefügt. Aktueller Stand: {summe}€")
if summe >= 100:
    print(f"Gesamtpreis: {summe}€. Glückwunsch! Du hast einen 10€ Gutschein gewonnen!")
else: 
    print(f"Gesamtpreis: {summe}€. Vielen Dank für deinen Einkauf!")