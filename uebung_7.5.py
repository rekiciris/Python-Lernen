class Buch:
    def __init__(self, titel):
        self.titel = titel
        self.ist_verliehen = False

class Kunde:
    def __init__(self, name):
        self.kunde_name = name
    def ausleihen(self, buch_objekt):
        buch_objekt.ist_verliehen = True
        return buch_objekt.titel
    
buch1 = Buch("Harry Potter")
buch2 = Buch("Zvezdica zaspanka")
kunde1 = Kunde("Alex")
kunde2 = Kunde("Elena")

geliehenes_buch = kunde1.ausleihen(buch1)

print(f"{kunde1.kunde_name} hat das Buch {geliehenes_buch} ausgeliehen. ")
print(buch1.ist_verliehen)