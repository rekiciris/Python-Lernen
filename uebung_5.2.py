def berechne_punkte(gegner_besiegt, bonus_items):
    summe = (gegner_besiegt * 100) + (bonus_items * 50)
    return summe

# Level 1: 3 Gegner, 2 Items
level1 = berechne_punkte(3,2)
# Level 2: 5 Gegner, 4 Items
level2 = berechne_punkte(5,4)
gesamt = level1 + level2

print(f"Punkte Level 1: {level1}")
print(f"Punkte Level 2: {level2}")
print(f"Deine Gesamtpunkte sind: {gesamt}")