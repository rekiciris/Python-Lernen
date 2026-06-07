class Film:
    def __init__(self, titel, genre):
        self.titel = titel
        self.genre = genre

        with open ("meine_fime.txt", "a") as datei:
            datei.write(f"{self.titel} - {self.genre}\n")
    
    def filme_anzeigen(self):
        with open ("meine_filme.txt", "r") as datei:
            for zeile in datei:
                print(f"Film: {zeile.strip()}")

film4 = Film("La La Land", "Musical")

film4.filme_anzeigen()