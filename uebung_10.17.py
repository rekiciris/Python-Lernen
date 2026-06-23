import json
import os

class Ticket:
    def __init__(self, titel, saal, preis):
        self.titel = titel
        self.saal = saal
        self.preis = preis

verkaufte_tickets = []

if os.path.exists("tickets.json"):
    with open ("tickets.json", "r") as datei:
        daten = json.load(datei)
    for x in daten:
        tickets = Ticket(x["titel"], x["saal"], x["preis"])
        verkaufte_tickets.append(tickets)
    print(f"Verkaufte Tickets für {tickets.titel}.")
else:
    verkaufte_tickets = []
    print("Noch keine Tickets im System.")

while True:
    print("1: Ticket kaufen")
    print("2: Verkaufte Tickets anzeigen")
    print("3: Ticket stornieren/löschen")
    print("4: Speichern & Beenden")

    wahl = input("Was möchtest du tun? ")

    if wahl == "1":
        titel = input("Welchen Film möchtest du schauen? ")
        saal = int(input("In welchem Saal spielt der film? "))
        preis = int(input("Was kostet das Ticket? "))
        neues_ticket = Ticket(titel, saal, preis)
        verkaufte_tickets.append(neues_ticket)
        print(f"Ticket für {titel} im Saal {saal} für {preis}€ wurde gekauft!")

    elif wahl == "2":
        nummer = 1
        print("\n--- TICKETS ---")
        for i in verkaufte_tickets:
            print(f"{nummer}: {i.titel}, Saal {i.saal}, {i.preis}€.")
            nummer += 1

    elif wahl == "3":
        loeschen = int(input("Welches Ticket wilst du löschen oder stornieren? Bitte gib die Nummer ein: "))
        index = loeschen - 1
        geloeschtes_ticket = verkaufte_tickets.pop(index)
        print(f"{geloeschtes_ticket.titel} wurde gelöscht!")

    elif wahl == "4":
        liste_fuer_json = []
        for i in verkaufte_tickets: 
            tickets_dict = {
                "titel": i.titel,
                "saal": i.saal,
                "preis": i.preis,
            }
            liste_fuer_json.append(tickets_dict)
        with open("tickets.json", "w") as datei:
            json.dump(liste_fuer_json, datei, indent=4)
        print("Tickets erfolgreich gespeichert!")
        break