reise_kosten = [120, 50, 250, 80, 150]
budget = 500

for x in reise_kosten:
    budget -= x

    if budget >= 0:
        print(f"Das kann ich mir leisten. Rest: {budget}€")
    else:
        print("Stopp! Das ist zu teuer.")