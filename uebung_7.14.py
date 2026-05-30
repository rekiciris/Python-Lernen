class Konto:
    def __init__(self, inhaber, kontostand):
        self.name = inhaber
        self.__geld = kontostand

    def kontostand_anzeigen(self):
        return self.__geld

    def einzahlen(self, betrag):
        if betrag > 0:
            self.__geld = self.__geld + betrag


mein_konto = Konto("Alex", 500)

mein_konto.einzahlen(200)

aktuelles_geld = mein_konto.kontostand_anzeigen()
print(f"Nach der Einzahlung hat {mein_konto.name}: {aktuelles_geld}€")