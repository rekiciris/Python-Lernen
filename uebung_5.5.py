VIP_gaeste = ["anna", "bob", "lina"]

def check_eintritt(name):
    if name in VIP_gaeste:
        return 0
    else:
        return 15
    
name = input("Gib deinen Namen ein. ").lower()

preis = check_eintritt(name)

print(f"Hallo {name}, dein Eintritt kostet {preis}€")