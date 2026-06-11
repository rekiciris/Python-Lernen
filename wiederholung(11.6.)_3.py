def berechne_schaden(angriff, verteidigung):
    schaden = angriff - verteidigung
    if schaden < 0:
        schaden = 0
    return schaden

finaler_schaden = berechne_schaden(50,20)
print(f"Der Gegner erleidet {finaler_schaden} Schaden!")