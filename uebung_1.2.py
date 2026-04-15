alter = int(input("Bitte gib dein alter ein. "))
if alter < 12:
    ticket = 5
elif alter >= 12 and alter < 18:
    ticket = 7
elif alter >= 18:
    ticket = 10
print("Dein Ticket kostet heute", ticket,"Euro.")