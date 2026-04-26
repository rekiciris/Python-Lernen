aktivitaeten = []
kosten = []
summe = 0

while True:
    neue_aktivitaet = input("Was willst du im Urlaub machen? ")
    if neue_aktivitaet.lower() == "stopp":
        break
    preis = float(input("Was kostet das? "))

    aktivitaeten.append(neue_aktivitaet)
    kosten.append(preis)

    if preis > 100:
        print("Oha, das ist teuer!")

print("\n --- KOSTEN ---")
for i in range(len(kosten)):
    print(f"{aktivitaeten[i]}: {kosten[i]}€")
    summe += kosten[i]

print(f"Gesammtkosten: {summe}€")