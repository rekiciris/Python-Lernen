class Konto:
    def __init__(self, inhaber, kontostand):
        self.name = inhaber
        self.__geld = kontostand

    def kontostand_anzeigen(self):
        return self.__geld


mein_konto = Konto("Alex", 500)

aktuelles_geld = mein_konto.kontostand_anzeigen()
print(f"Der Kontostand von {mein_konto.name} beträgt: {aktuelles_geld}€")