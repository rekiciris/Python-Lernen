def umrechnen(euro, kurs):
    if euro < 0:
        return "Ungültiger Betrag"
    else:
        return euro * kurs

geld_beutel = -50

dollar = umrechnen(geld_beutel, 1.10)
yen = umrechnen(geld_beutel, 160.0)

print(f"Du hast {dollar} Dollar und {yen} Yen.")