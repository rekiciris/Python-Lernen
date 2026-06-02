try:
    # Hier kommt der Code rein, der vielleicht abstürzen könnte
    zahl = int(input("Bitte eine Zahl eingeben: "))
except:
    # Hier springt Python NUR rein, wenn oben ein Fehler passiert ist!
    print("Hey, das war keine Zahl!")