class Kinosaal:
    def __init__ (self, titel, plaetze):  
        self.film_name = titel
        self.freie_plaetze = plaetze

class Besucher:
    def __init__ (self, name):
        self.besucher_name = name
    def tickets_kaufen(self, titel, tickets):
        self.anzahl = tickets
        if titel.freie_plaetze >= tickets:
            titel.freie_plaetze = titel.freie_plaetze - tickets
            return tickets
        else:
            return 0

kino1 = Kinosaal ("Avatar", 5)
besucher1 = Besucher ("Alex")

gekaufte_tickets = besucher1.tickets_kaufen(kino1, 5)

print(f"{besucher1.besucher_name} hat {gekaufte_tickets} Tickets für {kino1.film_name} gekauft.")