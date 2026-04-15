name = input("What is your name? ")
print(f"Hello {name}!")
age = int(input("How old are you? "))
if age < 18:
    print("Sadly you are underage and cannot continue.")
else:
    agreement = input("Do you agree with the terms of use? ").lower()
    if agreement.lower() == "no": 
        print("Sadly you cannot continue.")
    else:
        print("You may continue to the site. Good luck!")