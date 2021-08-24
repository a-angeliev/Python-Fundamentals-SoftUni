age = float(input())
male = input()
if male == 'm':
    if age >=16:
        print('Mr.')
    else:
        print('Master')
elif male == 'f':
    if age >= 16:
        print('Ms.')
    else:
        print('Miss')