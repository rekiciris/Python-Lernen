class Paket:
    def __init__(self, name, gewicht):
        self.empfaenger = name
        self.gewicht = gewicht
        self.ist_ausgeliefert = False
    def ausliefern (self):
        self.ist_ausgeliefert = True
        print(f"Das Paket für {self.empfaenger} wurde ausgeliefert!")

paket1 = Paket("Max", 5)
paket2 = Paket("Elena", 12)

print(f"Paket 1: {paket1.empfaenger}, {paket1.gewicht}kg")
print(f"Paket 2: {paket2.empfaenger}, {paket2.gewicht}kg")

paket1.ausliefern()

print(f"Paket von {paket1.empfaenger} - Ausgeliefert: {paket1.ist_ausgeliefert}!")
print(f"Paket von {paket2.empfaenger} - Ausgeliefert: {paket2.ist_ausgeliefert}!")