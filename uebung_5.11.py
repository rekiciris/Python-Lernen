passwoerter = ["123", "geheimnis123", "password", "hi", "python_fan_2026"]

def check_sicherheit(liste):
    zaehler =  0
    for x in liste:
        if (len(x)) >= 8:
            zaehler = zaehler + 1
    return zaehler
        
ergebnis = check_sicherheit(passwoerter)

print(f"Es wurden {ergebnis} sichere Passwörter gefunden.")