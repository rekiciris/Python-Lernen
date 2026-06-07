class Produkt:
    def __init__(self, name, preis):
        self.name = name
        self.preis = preis
    def kassenzettel_speichern(self):
        with open("warenkorb.txt", "a") as datei:
            datei.write(f"{self.name} kostet {self.preis}€\n")
            print("Produkt gespeichert!")

p1 = Produkt("Gaming Tastatur", 49.99)

p1.kassenzettel_speichern()