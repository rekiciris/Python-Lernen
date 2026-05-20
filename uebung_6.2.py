spieler = {"name": "Alex", "gold": 45}

def kaufen(held_dict, preis):
    if held_dict["gold"] >= preis:
        held_dict["gold"] = held_dict["gold"] - preis
        print(f"Kauf erfolgreich! Du hast noch {held_dict["gold"]} Gold.")
    else:
        print("Zu wenig Gold!")

print(spieler["gold"])

#Zauberschwert
kaufen(spieler, 30)
#Heiltrank
kaufen(spieler, 20)