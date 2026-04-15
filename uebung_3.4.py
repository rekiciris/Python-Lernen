passwort = "python123"
eingabe = ""
versuche = 0

while eingabe != "python123" and versuche < 3:
    eingabe = input("Gib dein Passwort ein! ")
    versuche = versuche + 1
    if eingabe != passwort:
        print(f"Falsch! Du hast noch {3 - versuche} Versuche übrig!")
if eingabe == "python123":
    print("Zugriff erlaubt! Willkommen!")
else:
    print("System gespert! Zu viele Versuche!")