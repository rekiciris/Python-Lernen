class Auto:
    def __init__(self, modell):
        self.auto_modell = modell
        self.ist_besetzt = False
class Kunde:
    def __init__(self,name):
        self.kunden_name = name
    def auto_mieten(self, auto_objekt):
        if auto_objekt.ist_besetzt == False:
            auto_objekt.ist_besetzt = True
            return auto_objekt.auto_modell
        else: 
            return "Bereits besetzt!"

auto1 = Auto("BMW i3")
kunde1 = Kunde("Bob")

gemietetes_modell = kunde1.auto_mieten(auto1)

print(f"{kunde1.kunden_name} hat das {auto1.auto_modell} gemietet!")
print(auto1.ist_besetzt)