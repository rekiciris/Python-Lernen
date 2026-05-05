def umrechnen(euro, kurs):
    x = euro * kurs
    return x

geld_beutel = 500

dollar = umrechnen(geld_beutel, 1.10)
yen = umrechnen(geld_beutel, 160.0)

print(f"Du hast {dollar} Dollar und {yen} Yen.")
