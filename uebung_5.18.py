import random
helden = ["Max", "Elena", "Dalia", "Dennis"]
def schatz_suche(name, schwierigkeit):
    glueck = random.randint(1, 10)
    if glueck >= schwierigkeit:
        print(f"{name} findet einen funkelnden Diamanten! (Glück: {glueck})")
        return 1
    else: 
        print(f"{name} findet nur alte Socken... (Glück: {glueck})")
        return 0
schatz_truhe = 0

for x in helden:
    fund = schatz_suche(x, 6)
    schatz_truhe = schatz_truhe + fund

print(f"Die Helden haben {schatz_truhe} Schätze gefunden!")