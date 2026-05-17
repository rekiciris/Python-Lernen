import random

helden_hp = 100
runden = [1, 2, 3, 4, 5]

def schaden_berechnen(angriff, max_block):
    block = random.randint(1, max_block)
    echter_schaden = angriff - block
    if echter_schaden < 0:
        echter_schaden = 0
    return echter_schaden

for r in runden:
    schaden = schaden_berechnen(25, 22)
    helden_hp = helden_hp - schaden
    if helden_hp <= 0:
        print("Du hast verloren!")
    else:
        print(f"Du hast {schaden} erlitten und hast noch {helden_hp} HP!")