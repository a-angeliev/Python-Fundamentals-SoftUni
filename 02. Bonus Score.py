number = int(input())
if number <=100:
    bonus = 5
elif 100<number<=1000:
    bonus = number *20/100
else:
    bonus = number *10/100

if number % 2 == 0:
    secound_bonus = 1
else :
    secound_bonus = 0

if number % 5 == 0 and number %2 != 0:
    trd_bonus = 2
else:
    trd_bonus = 0

print(bonus+secound_bonus+trd_bonus)
print(bonus+secound_bonus+trd_bonus+number)
print(number)
print(bonus)
print(secound_bonus)
print(trd_bonus)