class Auto:
    def __init__(self, modell):
        self.auto_modell = modell
        self.ist_besetzt = False

class ElektroAuto(Auto): 
    def __init__(self, modell, akku):
        super().__init__(modell)
        self.akkustand = akku

e_auto1 = ElektroAuto("BMW IX3", 85)

print(e_auto1.auto_modell)
print(e_auto1.akkustand)