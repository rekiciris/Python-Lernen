# 1. Eine Datei im Schreib-Modus ("w") öffnen
with open("notiz.txt", "w") as datei:
    # 2. Text in die Datei hineinschreiben
    datei.write("Hallo! Das ist mein allererster gespeicherter Text.\n")
    datei.write("Diese Zeile wird dauerhaft auf der Festplatte gespeichert!")

print("Datei wurde erfolgreich erstellt!")