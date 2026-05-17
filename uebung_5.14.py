alter_der_gaeste = [16, 21, 18, 17, 30]

for x in alter_der_gaeste:
    if x >= 18:
        print(f"Gast ist {x} Jahre alt: Einlass gewährt!")
    else: 
        print(f"Gast ist erst {x} Jahre alt: ZU jung!")