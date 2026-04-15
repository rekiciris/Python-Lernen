punktzahl = int(input("Wie viele Punkte hast du erreicht? "))
if punktzahl >= 90 and punktzahl <=100:
    print("Note 1!")
elif punktzahl >= 80 and punktzahl <= 89:
    print("Note 2!")
elif punktzahl >= 70 and punktzahl <= 79:
    print("Note 3!")
else:
    print("Du musst mehr üben!")