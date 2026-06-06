print("Verdopplungs-Mode!")
try:
    zahl = int(input("Gib deine Lieblingszahl ein: "))
    print(f"Deine Zahl verdoppelt ist: {zahl * 2}!")
except ValueError:
    print("Deine Zahl muss eine Ganzezahl sein!")