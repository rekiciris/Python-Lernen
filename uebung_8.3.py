try:
    preis = float(input("Bitte Produktpreis eingeben: "))
    rabatt_preis = preis * 0.9
    print(f"Der Preis mit Rabatt ist: {rabatt_preis}€")
except:
    print("Ungültige Eingabe! Bitte verwende nur Zahlen.")