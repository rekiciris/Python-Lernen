class Kämpfer:
    def __init__ (self, name, leben):
        self.kaempfer_name = name
        self.hp = leben
    def angreifen(self, gegner_objekt, schaden):
        gegner_objekt.hp = gegner_objekt.hp - schaden
        return gegner_objekt.kaempfer_name
    
spieler1 = Kämpfer("Warrior", 100)
spieler2 = Kämpfer("Goblin", 30)

getroffener = spieler1.angreifen(spieler2, 20)

print(f"Der Kämpfer {getroffener} wurde getroffen!")
print(f"Der Goblin hat jetzt noch {spieler2.hp} HP übrig.")