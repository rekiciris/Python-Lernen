class Buch:
    def __init__(self, titel, autor):
        self.titel = titel
        self.autor = autor

meine_bibliothen = []

buch1 = Buch("Harry Potter", "J.K. Rowling")
buch2 = Buch("Der Herr der Ringe", "J.R.R. Tolkien")

meine_bibliothen.append(buch1)
meine_bibliothen.append(buch2)

for x in meine_bibliothen:
    print(f"{x.titel} von {x.autor} steht im Regal!")