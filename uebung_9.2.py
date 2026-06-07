# Wir öffnen dieselbe Datei, aber im Modus "a" für Append (Anhängen)
with open("notiz.txt", "a") as datei:
    # Wir fügen eine neue Zeile hinzu
    datei.write("\nDas hier ist ein Nachtrag vom Sonntagabend!")

print("Text wurde erfolgreich angehängt!")