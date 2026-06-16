import json
import os

class Kunde:
    def __init__(self, name, email, umsatz):
        self.name = name
        self.email = email
        self.umsatz = umsatz
    def einkaufen(self, betrag):
        self.betrag = betrag
        self.umsatz = betrag + self.umsatz
        print(f"{self.name} hat gerade für {self.betrag}€ eingekauft.")

if os.path.exists("kunde_speicher.json"):
    with open("kunde_speicher.json", "r") as datei:
        daten = json.load(datei)
    kunde1 = Kunde(daten["name"], daten["email"], daten["umsatz"])
    print(f"--- {kunde1.name} hat für {kunde1.betrag}€ eingekauft! ---")
else:
    kunde1 = Kunde("Max", "max@email.com", 0)
    print(f"--- {kunde1.name} hat gerade zum ersten mal bei uns eingekauft! ---")

while True:
    print("\n--- SUPERMARKT ---")
    print("1: Einkaufen!")
    print("2: Kunden-Infos anzeigen")
    print("3: Speichern & Beenden")
    
    wahl = input("Was möchtest du tun? (1-3): ")
    
    if wahl == "1":
        euro = int(input("Wie viel Geld hat der Kunde ausgegeben? "))
        kunde1.einkaufen(euro)
        
    elif wahl == "2":
        print(f"Der Kunde heißt {kunde1.name} ({kunde1.email}) und hat bisher {kunde1.umsatz}€ ausgegeben.")
        
    elif wahl == "3":
        kunde_als_dict = {
            "name": kunde1.name,
            "email": kunde1.email,
            "umsatz": kunde1.umsatz
        }
        with open("kunde_speicher.json", "w") as datei:
            json.dump(kunde_als_dict, datei, indent=4)
            
        print("Einkauf erfolgreich gespeichert. Tschüss! 👋")