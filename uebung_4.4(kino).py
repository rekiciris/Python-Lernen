neuer_film = input("Welchen Film möchtest du speichern? ")
with open("meine_filme.txt", "a") as datei:
    datei.write(neuer_film + "\n")

print("--- Film wurde gespeichert! ---")

print("Deine aktuele Liste:")
with open("meine_filme.txt", "r") as datei:
    inhalt = datei.read()
    print(inhalt)