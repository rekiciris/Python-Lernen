ime = input("Kako se zoves? ")
print("Pozdrav", ime,"!")
gledanje = input("Dali si gledao utakmicu Bosna Italija? ").lower()
if gledanje == "da":
    print("Odlicna utakmica!")
    prolaz = input("Dali mislis da ce Bosna proci grupnu fazu? ").lower()
    if prolaz == "da":
        print("Ma hoce sigurno 💪")
    else:
        print("Eh jebi ga sad 😒")
else:
    print("E onda nista 😂")