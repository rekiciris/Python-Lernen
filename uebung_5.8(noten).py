noten = [1, 3, 4, 5, 2, 6]

def bewertung_erstellen(note):
    if note == 1 or note == 2 or note == 3 or note == 4:
        return "Bestanden"
    else:
        return "Nicht bestanden"
    
for i in range(len(noten)):
    ergebnis = bewertung_erstellen (noten[i])

    print(f"Schüler Nr. {i+1}: Note {noten[i]} - {ergebnis}")