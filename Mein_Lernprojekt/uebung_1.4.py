temperatur = float(input("Wie ist die Temperatur heute? "))
regen = input("Regnet es? ")
if temperatur >= 20 and regen.lower() == "nein":
    print("Zieh ein T-Shirt an!")
elif regen.lower() == "ja":
    print("Nimm einen Regenschirm mit!")
elif temperatur < 5:
    print("Vergiss deine Jacke nicht!")
else:
    print("")