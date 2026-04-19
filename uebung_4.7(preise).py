preise = []
einzelpreis = 1
namen = []
summe = 0

while einzelpreis != 0:
    name = input("Was hast du gekauft? (oder stopp): ")

    if name.lower() == "stopp":
        break

    einzelpreis = float(input(f"Was hat {name} gekostet? "))

    namen.append(name)
    preise.append(einzelpreis)

print("\n---- KASSENBON ----")
for i in range(len(preise)):
    print(f"{namen[i]}: {preise[i]}")
    summe += preise[i]

print("-" * 20)
print(f"Gesamtsumme: {summe}€")