class StreamingKonto:
    def __init__(self, name, abo_typ):
        self.nutzer = name
        self.abo = abo_typ
        self.minuten_gesehen = 0
    def schauen(self, dauer):
        self.minuten_gesehen = self.minuten_gesehen + dauer
        print(f"{self.nutzer} hat {dauer} Minuten geschaut.")
    def upgrade(self, neues_abo):
        self.abo = neues_abo
        print(f"Erfolgreiches Upgrade für {self.nutzer}! Neues Abo: {self.abo}")

konto1 = StreamingKonto("Alex", "Basis")
konto2 = StreamingKonto("Elena", "Premium")

konto1.schauen(90)
konto2.schauen(120)
konto1.upgrade("Premium")

print(f"Das aktuelle Abo von {konto1.nutzer} ist {konto1.abo}. Es wurde {konto1.minuten_gesehen} Minuten geschaut.")
print(f"Das aktuelle Abo von {konto2.nutzer} ist {konto2.abo}. Es wurde {konto2.minuten_gesehen} Minuten geschaut.")