preise = [10, 20, 50]
def steuer_hinzufuegen(liste):
    for i in range(len(liste)):
        liste[i] = liste[i] * 1.2

steuer_hinzufuegen(preise)

print(preise)