class Produkt:
    def __init__(self, name, preis):
        self.produkt_name = name
        self.preis = preis
class Kleidung(Produkt):
    def __init__(self, name, preis, groesse):
        super().__init__(name, preis)
        self.groesse = groesse

p1 = Produkt("Python Buch", 29.99)
k1 = Kleidung("Hoodie", 49.99, "XL")

print(f"Das Kleidungsstück {k1.produkt_name} in Größe {k1.groesse} kostet {k1.preis}€.")