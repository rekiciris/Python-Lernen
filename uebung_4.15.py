gaeste = []
getraenke = []

while True:
    name = input("Wer ist eingeladen? ")
    if name.lower() == "stopp":
        break
    if name in gaeste:
        print("Steht schon auf der Liste!")
    else:
        gaeste.append(name)
        getraenk = input("Welches Getränk wünscht er/sie sich? ")
        getraenke.append(getraenk)

#jeder Gast kostet pauschal 15€

anzahl = len(gaeste)
gesamtkosten = anzahl * 15

print("\n --- PARTYLISTE ---")
for i in range(len(gaeste)):
    print(f"Gast Nr. {i + 1} : {gaeste[i]} wünscht sich {getraenke[i]}.")
print(f"Die Gesamtkosten für die Party sind {gesamtkosten}€")