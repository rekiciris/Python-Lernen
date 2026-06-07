class Produkt:
    def __init__(self, name, preis):
        self.name = name
        self.preis = preis

    def kassenzettel_speichern(self):
        with open("warenkorb.txt", "a") as datei:
            # HIER: Wir speichern NUR die Zahl, kein €-Zeichen!
            datei.write(f"{self.name} kostet {self.preis}\n")
        print("Produkt gespeichert!")

# --- Hauptprogramm ---
p1 = Produkt("Gaming Tastatur", 49.99)
p2 = Produkt("Gaming Maus", 29.99)

p1.kassenzettel_speichern()
p2.kassenzettel_speichern()


def kasse_abrechnen():
    gesamtsumme = 0
    with open("warenkorb.txt", "r") as datei:
        for zeile in datei:
            teile = zeile.strip().split("kostet ")
            if len(teile) > 1:
                preis_text = teile[1]
                gesamtsumme = gesamtsumme + float(preis_text)

    print("--- KASSENZETTEL ---")
    print(f"Gesamtsumme aller Produkte: {gesamtsumme}€")

kasse_abrechnen()