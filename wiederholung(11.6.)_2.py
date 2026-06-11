geheimnis = "python123"
eingabe = ""

while eingabe != geheimnis:
    eingabe = input("Bitte Passwort eingeben: ")
    if eingabe != geheimnis:
        print("Passwort falsch!")

print("Zugriff erlaubt! Willkommen im System!")