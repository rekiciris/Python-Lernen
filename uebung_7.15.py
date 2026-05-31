class Ticket:
    def __init__(self, filmname, preis):
        self.film = filmname
        self.__preis = preis
    def preis_anzeigen(self):
        return self.__preis
class VipTicket (Ticket):
    def __init__(self, filmname, preis, lounge_zugang):
        super().__init__(filmname, preis)
        self.lounge = lounge_zugang
class Kunde:
    def __init__(self, name):
        self.kunden_name = name
    def ticket_kaufen(self, ticket_objekt):
        preis = ticket_objekt.preis_anzeigen()
        return preis

vip1 = VipTicket("Avatar", 25, "Gold-Lounge")
k1 = Kunde("Paul")

bezahlter_betrag = k1.ticket_kaufen(vip1)

print(f"{k1.kunden_name} hat das VIP-Ticket für {vip1.film} ({vip1.lounge}) für {bezahlter_betrag}€ gekauft!")