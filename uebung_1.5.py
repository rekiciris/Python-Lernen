gesamtpreis = float(input("Was ist der Gesamtpreis des Einkaufs? "))
if gesamtpreis >= 100:
    print("Dein Endpreis ist:", gesamtpreis - 20, "Euro!")
elif gesamtpreis >= 50 and gesamtpreis < 100:
    print("Dein Endpreis ist:", gesamtpreis - 5, "Euro!")
else:
    print("Dein Endpreis ist", gesamtpreis,"Euro!")