food = int(input())
food = food*1000
text = '0'
while text != 'Adopted':
    food = food - int(text)
    text= input()

if food>= 0:
    print(f"Food is enough! Leftovers: {food} grams.")
else:
    print(f"Food is not enough. You need {abs(food)} grams more.")