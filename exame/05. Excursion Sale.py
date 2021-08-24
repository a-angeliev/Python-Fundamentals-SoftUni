money = 0
sea_trips = int(input())
muntain_trips = int(input())
while (sea_trips !=0 or muntain_trips !=0):
    a = input()
    if a == 'sea' and sea_trips>0:
        money = money + 680
        sea_trips = sea_trips - 1
    elif a == 'mountain' and muntain_trips>0:
        money = money + 499
        muntain_trips = muntain_trips -1
    elif a =='Stop':
        break
if sea_trips== 0 and muntain_trips ==0:
    print(f"Good job! Everything is sold.")
print(f"Profit: {money} leva.")
