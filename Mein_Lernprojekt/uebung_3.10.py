muenzen = [2, 1, 0.5, 2, 2, 1, 2]
kontostand = 0

for x in muenzen:
    kontostand = kontostand + x
    if kontostand > 5:
        print(f"Ziel von 5 Euro erreicht! Aktuel: {kontostand} Euro.")
print(f"Dein Kontostand ist {kontostand} Euro.")