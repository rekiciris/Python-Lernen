class Bankkonto:
    def __init__(self, inhaber, start_geld):
        self.kontoinhaber = inhaber   
        self.kontostand = start_geld    

    def einzahlen(self, betrag):
        self.kontostand = self.kontostand + betrag
        print(f"Erfolgreich {betrag}€ eingezahlt. Neuer Kontostand: {self.kontostand}€")

    def abheben(self, betrag):
        if self.kontostand >= betrag:
            self.kontostand = self.kontostand - betrag
            print(f"Erfolgreich {betrag}€ abgehoben. Rest: {self.kontostand}€")
        else:
            print("Fehler: Nicht genug Geld auf dem Konto!")


konto1 = Bankkonto("Alex", 500)
konto2 = Bankkonto("Elena", 1000)

print(f"Konto von {konto1.kontoinhaber} wurde geöffnet.")
konto1.einzahlen(200)
konto1.abheben(100)

print("-" * 30)

print(f"Konto von {konto2.kontoinhaber} hat aktuell: {konto2.kontostand}€")
konto2.abheben(1200)