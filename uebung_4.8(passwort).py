passwort = input("Gib dein neues Passwort ein! ")
if len(passwort) > 8 and ("!" in passwort or "?" in passwort):
    print("Passwort ist sicher!")
else:
    print("Das Passwort ist zu unsicher.")