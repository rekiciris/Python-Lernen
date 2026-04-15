lieblingsessen = input("Was ist dein Lieblingsessen? ")
anzahl = input("Wie viele Portionen davon könntest du essen? ")
print("Wow,", anzahl, "-mal", lieblingsessen, "zu essen ist echt stark!")
anzahl_zahl = int(anzahl)
kalorien_gesamt = anzahl_zahl * 500
print("Das wären insgesamt", kalorien_gesamt, "Kalorien! ")
