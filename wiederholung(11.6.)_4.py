class Auto:
    def __init__(self, marke, modell, kilometerstand):
        self.marke = marke
        self.modell = modell
        self.kilometerstand = kilometerstand
    def fahren (self, km):
        self.km = km
        self.kilometerstand = km + self.kilometerstand
        print(f"Der {self.marke} {self.modell} ist {km} gefahren.")
        print(f"Der {self.modell} hat jetzt einen Kilometerstand von {self.kilometerstand}.")

auto1 = Auto("VW", "Golf", 50000)

auto1.fahren(150)