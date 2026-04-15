alter = int(input("Wie alt bist du? "))
einladung = input("Hast du eine Einladung? ").lower()
if alter >= 18 and einladung == "ja":
    print("Willkommen auf der Party!")
else:
    print("Leider kein Zutritt.")