class Auto:
    def __init__(self, name, start_tank):
        self.auto_name = name
        self.tank = start_tank
    def fahren(self, verbrauch):
        self.auto_verbrauch = self.tank - verbrauch
        print(f"{self.auto_name} hat bis jetzt {verbrauch} Liter verbraucht.")

class Tankstelle:
    def __init__(self, name, benzin_vorrat):
        self.tankstellen_name = name
        self.vorrat = benzin_vorrat
    def auftanken(self, auto_objekt, liter):
        self.benzin_vorrat = self.vorrat - liter
        auto_objekt.tank = auto_objekt.tank + liter
        return liter

auto1 = Auto("X6", 50)
tankstelle1 = Tankstelle("Aral", 1000)

auto1.fahren(40)
getankt = tankstelle1.auftanken(auto1, 30)

print(f"Dein {auto1.auto_name} wurde auf der {tankstelle1.tankstellen_name} Tankstelle aufgetankt.")
print(f"Es wurden {getankt} Liter aufgetankt.")