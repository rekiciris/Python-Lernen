pakete = [10, 45, 12, 60, 33, 5]
schwere_pakete = 0

for x in pakete:
    if x >= 40:
        schwere_pakete = schwere_pakete + 1
    else:
        print("Dieses paket ist leicht.")
print(f"Es wurden {schwere_pakete} schwere Pakete gefunden.")