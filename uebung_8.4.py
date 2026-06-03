class TankSaeule:
    def __init__(self, preis_pro_liter):
        self.__preis = preis_pro_liter
    def preis_holen(self):
        return self.__preis
class BenzinSaeule (TankSaeule):
    def __init__(self, preis_pro_liter, typ):
        super().__init__(preis_pro_liter)
        self.kraftstoff = typ
class DieselSaeule (TankSaeule):
    def __init__(self, preis_pro_liter, typ):
        super().__init__(preis_pro_liter)
        self.kraftstoff = typ

DS1 = DieselSaeule(1.65, "Normal Diesel")
BS1 = BenzinSaeule(1.75, "Super E10")

try:
    liter = float(input("Wie viele Liter möchten Sie tanken? "))
    preis = BS1.preis_holen()
    gesamtkosten = liter * preis
    print(f"Sie haben {liter}L {BS1.kraftstoff} für insgesamt {gesamtkosten}€ getankt!")
except:
    print("Fehler! Bitte geben Sie die Literzahl als Zahl ein!")