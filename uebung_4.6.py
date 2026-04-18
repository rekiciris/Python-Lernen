gaeste = ["anna", "ben", "lara"]
name = input("Wie heißt du? ")

if name.lower() in gaeste:
    print("Du darfst rein!")
else:
    print("Du stehst nicht auf der Liste!")