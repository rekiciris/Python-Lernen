class Fahrzeug:
    def __init__(self, modell, preis_pro_tag):
        self.modell = modell
        self.__preis = preis_pro_tag
    def preis_holen(self):
        return self.__preis
class ElektroAuto (Fahrzeug):
    def __init__(self, modell, preis_pro_tag, batterie_stand):
        super().__init__(modell, preis_pro_tag)
        self.batterie = batterie_stand
class Kunde:
    def __init__(self, name):
        self.kunden_name = name
    def auto_mieten(self, auto_objekt, tage):
        preis = auto_objekt.preis_holen()
        gesamtkosten = tage * preis
        return gesamtkosten

EA1 = ElektroAuto("Tesla MOdel 3", 89.0, "100%")
K1 = Kunde("Bob")

try:
    tage = int(input("Wie viele Tage möchten Sie das Auto mieten? "))
    gesamtkosten = K1.auto_mieten(EA1, tage)
    print(f"{K1.kunden_name} mietet den {EA1.modell} ({EA1.batterie} Akku) für {tage} Tage. Gesamtpreis: {gesamtkosten}€")
except:
    print("Bitte geben Sie die Anzahl der Tage als ganze Zahl ein!")