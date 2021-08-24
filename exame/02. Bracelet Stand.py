pocket_money = float(input())
sells_money = float(input())
spend_money = float(input())
gift_price = float(input())
saved_pocket_money = pocket_money * 5
saved_money_fromsellse = sells_money * 5
all_saved_money = saved_money_fromsellse +saved_pocket_money
money_gift = all_saved_money - spend_money
if money_gift>= gift_price:
    print(f"Profit: {money_gift:.2f} BGN, the gift has been purchased.")
else:
    print(f"Insufficient money: {gift_price - money_gift :.2f} BGN.")