class PremiumAbo:
    def __init__(self, name, preis):
        self.abo_name = name
        self.__monats_preis = preis
    def preis_anzeigen(self):
        return self.__monats_preis

abo1 = PremiumAbo("Netflix UHD", 19.99)

try:
    monate = int(input("Für wie viele Monate möchten Sie im Voraus bezahlen? "))
    preis = abo1.preis_anzeigen()
    gesamtkosten = monate * preis
    print(f"Das Abo {abo1.abo_name} kostet für {monate} Monate insgesamt {gesamtkosten}€.")
except:
    print("Fehler: Bitte geben Sie die Anzahl der Monate als Zahl ein!")