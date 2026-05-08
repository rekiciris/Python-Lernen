gaeste = ["aNNa", "BoB", "LINA"]

def namen_sauber_machen(liste):
    for i in range(len(liste)):
        liste[i] = liste[i].capitalize()
        
namen_sauber_machen(gaeste)

print(gaeste)