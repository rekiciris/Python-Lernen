preise = [12.50, 4.99, 25.00, 8.00]
mein_geld = 40.00

def kauf_check(preis, budget):
    if preis <= budget:
        budget = budget - preis
        return budget
    else: 
        return "Zu teuer!"

for x in preise:
    ergebnis = kauf_check(x, mein_geld)
    if ergebnis == "Zu teuer!":
        print(f"Der Artikel für {x} ist zu teuer! Rest: {mein_geld}€")
    else:
        mein_geld = ergebnis
        print(f"Gekauft für {x}€! Rest: {mein_geld}€")