einkaufsliste = []

while True:
    artikel = input("Was fehlt im Kühlschrank? ")
    if artikel.lower() == "fertig":
        break

    if artikel in einkaufsliste:
        print("Schon da!")
    else:
        einkaufsliste.append(artikel)

print("\n --- EINKAUFSLISTE --- ")
for i in range(len(einkaufsliste)):
    print(f"{i + 1}. {einkaufsliste[i]}")