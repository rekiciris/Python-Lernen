with open("text.txt", "r") as datei:
    inhalt = datei.read()

print("Das steht in der Datei drin:")
print("----------------------------")
print(inhalt)
print("----------------------------")