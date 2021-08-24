location_number = int(input())
for i in range(1, location_number + 1):
    avr_mining = 0
    for k in range(0, 1):
        avr_mining = float(input())
        days_mining = int(input())
        all_mining_gold = 0
        for z in range(0, days_mining):
            mining_gold_per_day = float(input())
            all_mining_gold = all_mining_gold + mining_gold_per_day
        if avr_mining <= (all_mining_gold / days_mining):
            print(f"Good job! Average gold per day: {all_mining_gold / days_mining:.2f}.")
        else:
            print(f"You need {avr_mining - (all_mining_gold / days_mining):.2f} gold.")
