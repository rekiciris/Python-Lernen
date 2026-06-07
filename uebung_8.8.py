kontostand = 100

try:
    personen = int(input("Auf wie viele Personen soll das Geld aufgeteilt werden? "))
    anteil = kontostand / personen
    print(f"Jede Person bekommt: {anteil}€.")
except ValueError:
    print("Fehler: Bitte gib eine ganze Zahl ein!")
except ZeroDivisionError:
    print("Fehler: Du kannst Geld nicht auf 0 Personen aufteilen!")