bestand = [5, 12, 8, 20, 3]

def lager_pruefen(liste):
    for i in range(len(liste)):
        if liste[i] < 10:
            liste[i] = liste[i] + 50
            print(f"Position {i+1} wurde aufgefüllt!")

lager_pruefen(bestand)

print(bestand)