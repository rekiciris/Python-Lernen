import random

spieler = ["Max", "Elena", "Alex", "Dennis"]

def wuerfel_check(name, gewinn_zahl):
    wuerfel = random.randint(1, 10)
    if wuerfel >= gewinn_zahl:
        print(f"{name} hat eine {wuerfel} gewürfelt: GEWONNEN!")
        return 1
    else:
        print(f"{name} hat eine {wuerfel} gewürfelt: Verloren...")
        return 0
    
gewinner_zaehler = 0
for x in spieler:
    ergebnis = wuerfel_check(x, 6)

gewinner_zaehler = gewinner_zaehler + ergebnis