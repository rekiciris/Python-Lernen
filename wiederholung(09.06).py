alter = int(input("Wie alt bist du? "))

if alter < 16:
    print("Du bist zu Jung! Ab nach Hause!")
elif alter == 16 or alter == 17:
    print("Du darfst nut mit Muttizettel rein!")
else:
    print("Willkommen im Club!")