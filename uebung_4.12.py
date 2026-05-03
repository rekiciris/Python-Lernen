aktivitaeten = []
preise = []
budget = 300

while True:
    neue_aktivitaet = input("Was willst du im Urlaub machen? ")
    if neue_aktivitaet.lower() == "fertig":
        break
    preis = float(input("Was kostet das? "))
    if preis <= budget:
        budget = budget - preis

        aktivitaeten.append(neue_aktivitaet)
        preise.append(preis)
        print(f"Gebucht! Restbudget: {budget}€")
    else:
        print(f"Zu teuer! Du hast nur noch {budget}€")

print("\n--- URLAUBSKOSTEN ---")
for i in range(len(preise)):
    print(f"{aktivitaeten[i]}: {preise[i]}€")