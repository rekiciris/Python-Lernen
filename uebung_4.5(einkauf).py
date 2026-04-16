artikel = ""
while artikel.lower() != "stopp":
    artikel = input("Schreibe die Artikel die du kaufen willst. " )

    if artikel.lower() != "stopp":
        with open("einkaufs_liste.txt", "a") as liste:
            liste.write(artikel + "\n")

    print(f"Artikel: {artikel}")
print("Die Einkaufsliste ist fertig!")

with open ("einkaufs_liste.txt", "r") as liste:
    print("---EINKAUFSLISTE---")
    print("-------------------")
    for x in liste:
        print(x.strip())