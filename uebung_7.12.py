class Konto:
    def __init__(self, inhaber, kontostand):
        self.name = inhaber
        self.__geld = kontostand

mein_konto = Konto("Alex", 500)
print(mein_konto.name)
print(mein_konto.__geld)