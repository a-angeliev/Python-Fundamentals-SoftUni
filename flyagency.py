company = input()
old_tik = int(input())
kid_tik = int(input())
old_price = float(input())
tax = float(input())
kid_price = old_price *70/100

all_old_price =old_tik * old_price
all_kid_price = kid_tik * kid_price
all_tax = (old_tik + kid_tik) * tax
profit = (all_kid_price+ all_old_price+all_tax)
print(f"The profit of your agency from {company} tickets is {profit} lv.")
print(all_tax)