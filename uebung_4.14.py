aktivitaeten = []
preise = []
bewertungen = []
budget = 300

while True:
    neue_aktivitaet = input("Was willst du im Urlaub machen? ")
    if neue_aktivitaet.lower() == "fertig":
        break
    preis = float(input("Was kostet das? "))
    if preis <= budget:
        budget = budget - preis

        bewertung = int(input(f"Wie würdest du {neue_aktivitaet} von 1-10 bewerten? "))

        aktivitaeten.append(neue_aktivitaet)
        preise.append(preis)
        bewertungen.append(bewertung)

        print(f"Gebucht! Restbudget: {budget}€")
    else:
        print(f"Zu teuer! Du hast nur noch {budget}€")

print("\n--- URLAUBSKOSTEN ---")
for i in range(len(aktivitaeten)):
    info = f"{aktivitaeten[i]} ({preise[i]}) - Note: {bewertungen[i]}"
    if bewertungen[i] == 10:
        print(f"{info} <-- Das wird super!")
    else:
        print(info)
    if len(bewertungen) > 0:
        durchschnitt = sum(bewertungen) / len(bewertungen)
        print(f"\nAnzahl der Aktivitäten: {len(aktivitaeten)}")
        print(f"Deine durchschnittliche Vorfreude-Note: {durchschnitt:.1f}")