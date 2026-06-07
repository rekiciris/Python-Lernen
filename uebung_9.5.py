class Film:
    def __init__(self, titel, genre):
        self.titel = titel
        self.genre = genre

        with open ("meine_fime.txt", "a") as datei:
            datei.write(f"{self.titel} - {self.genre}\n")

film1 = Film("Inception", "Sci-Fi")
film2 = Film("Barbie", "Comedy")
film3 = Film("Mummie", "Horror")