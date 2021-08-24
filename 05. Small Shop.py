product = input()
city = input()
quality = float(input())
if city == "Sofia":
    if product == 'coffee':
        print(quality*0.5)
    elif product=='water':
        print(quality*0.8)
    elif product == 'beer':
        print(quality * 1.2)
    elif product == 'sweets':
        print(quality * 1.45)
    elif product == 'peanuts':
        print(quality * 1.6)
elif city == 'Plovdiv':
    if product == 'coffee':
        print(quality*0.4)
    elif product=='water':
        print(quality*0.7)
    elif product == 'beer':
        print(quality * 1.15)
    elif product == 'sweets':
        print(quality * 1.30)
    elif product == 'peanuts':
        print(quality * 1.5)
elif city == 'Varna':
    if product == 'coffee':
        print(quality*0.45)
    elif product=='water':
        print(quality*0.70)
    elif product == 'beer':
        print(quality * 1.10)
    elif product == 'sweets':
        print(quality * 1.35)
    elif product == 'peanuts':
        print(quality * 1.55)