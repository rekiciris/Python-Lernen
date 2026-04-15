geheimzahl = 7
tipp = 0
versuche = 0

while tipp != 7:
    tipp = int(input("Rate meine Geheimzahl: "))
    versuche = versuche +1
    if tipp > 7:
        print("Zu hoch! Versuch es nochmal.")
    elif tipp < 7:
        print("Zu niedrig! Versuch es nochmal.")
print(f"Richtig! Du hast gewonnen und hast {versuche} Versuche gebraucht!")