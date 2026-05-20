spieler = {"name": "Alex", "gold": 100, "inventar": []}

def kaufen(held_dict, gegenstand, preis):
    if held_dict["gold"] >= preis:
        held_dict["gold"] = held_dict["gold"] - preis
        held_dict["inventar"].append(gegenstand)
        print(f"Kauf erfolgreich! Du hast {gegenstand} gekauft und hast noch {held_dict["gold"]} Gold.")
    else:
        print(f"Zu wenig Gold für {gegenstand}!")

print(spieler["gold"])

kaufen(spieler, "Zauberschwert", 40)
kaufen(spieler, "Heiltrank", 20)
kaufen(spieler, "Schild", 50)

print(spieler)