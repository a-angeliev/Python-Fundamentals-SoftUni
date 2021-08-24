computers = int(input())
all_sellse = 0
avrg_rateing = 0
for i in range(0, computers):
    a = int(input())
    rateing = a % 100
    posible_sellse = a // 10
    if rateing ==2:
        percent_fromselles = 0
    elif rateing == 3:
        percent_fromselles = 50/100
    elif rateing ==4:
        percent_fromselles = 70/100
    elif rateing ==5:
        percent_fromselles = 85/100
    elif rateing == 6:
        percent_fromselles = 100/100
    sellse = percent_fromselles * posible_sellse
    all_sellse = all_sellse +sellse
    avrg_rateing = avrg_rateing + rateing
print(f"{all_sellse:.2f}")
print(f"{avrg_rateing/ computers:.2f}")