print("--- Zeilenweise Auswertung ---")

with open("notiz.txt", "r") as datei:
    # Wir gehen jede Zeile einzeln durch
    for zeile in datei:
        # .strip() schneidet unsichtbare Leerzeichen und doppelte Zeilenumbrüche am Ende ab
        print(f"Gelesene Zeile: {zeile.strip()}")