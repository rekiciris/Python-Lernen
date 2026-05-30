class Paket:
    def __init__(self, empfaenger):
        self.kunde = empfaenger
        self.ist_geliefert = False
class ExpressPaket(Paket):
    def __init__(self, empfaenger, uhrzeit):
        super().__init__(empfaenger)
        self.liefer_zeit = uhrzeit
class Postbote:
    def __init__(self, name):
        self.nachname = name
    def zustellen (self, paket_objekt):
        paket_objekt.ist_geliefert = True
        return paket_objekt.kunde

ep1 = ExpressPaket("Alex", "12:00 Uhr")
pb1 = Postbote("Müller")

zustellung = pb1.zustellen(ep1)

print(f"Postbote {pb1.nachname} hat das Expresspaket (Lieferung bis {ep1.liefer_zeit}) erfolgreich an {ep1.kunde} Ausgeliefert!")

print(ep1.ist_geliefert) 