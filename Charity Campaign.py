days_number = int(input())
cookers = int(input())
cakes_number = int(input())
gof_number = int(input())
pancakes_number = int(input())
cake_price = 45
gof_price = 5.8
pancakes_price = 3.20
cakes_perday = cookers * cakes_number
gof_perday = cookers * gof_number
pancakes_perday = cookers * pancakes_number
cakes_allprice = cakes_perday * days_number * cake_price
gof_allprice = gof_perday * days_number * gof_price
panckes_allprice = pancakes_perday * days_number * pancakes_price
allprice = gof_allprice + cakes_allprice + panckes_allprice
sum = allprice * (7/8)

print(sum)