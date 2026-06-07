# Wir öffnen die Datei im Modus "r" für Read (Lesen)
with open("notiz.txt", "r") as datei:
    # Wir laden den kompletten Inhalt in eine Variable
    inhalt = datei.read()

# Jetzt drucken wir den Inhalt im Terminal aus
print("--- Inhalt der Datei notiz.txt ---")
print(inhalt)
print("---------------------------------")