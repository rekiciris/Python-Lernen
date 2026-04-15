benutzername = input("Gib deinen Benutzernamen ein.")
if benutzername == "Iris":
    passwort = input("Gib dein Passwort ein.")
    if passwort == "Python123":
        print("Willkommen im Cockpit!")
    else:
        print("Zugriff verweigert!")
else:
    print("Benutzername falsch")