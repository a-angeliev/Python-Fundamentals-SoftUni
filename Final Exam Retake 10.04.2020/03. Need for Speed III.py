car_numbers = int(input())
cars = {}
for _ in range(car_numbers):
    car,miles,fuel = input().split("|")
    miles = int(miles)
    fuel =int(fuel)
    cars[car] = {"miels":miles, "fuel":fuel}

command = input().split(" : ")
while not command[0] == "Stop":
    if command[0] == "Drive":
        car = command[1]
        distance = int(command[2])
        fuel = int(command[3])
        if car in cars:
            if cars[car]['fuel'] < fuel:
                print("Not enough fuel to make that ride")
            else:
                cars[car]['fuel'] -= fuel
                cars[car]['miels'] += distance
                print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
                if cars[car]['miels'] >= 100000:
                    print(f"Time to sell the {car}!")
                    del cars[car]

    if command[0] == "Refuel":
        car = command[1]
        fuel = int(command[2])
        if car in cars:
            if cars[car]["fuel"] + fuel <= 75:
                cars[car]['fuel'] += fuel
                print(f"{car} refueled with {fuel} liters")
            else:
                fuel = 75 - cars[car]['fuel']
                cars[car]["fuel"] = 75
                print(f"{car} refueled with {fuel} liters")

    if command[0] == "Revert":
        car = command[1]
        kilo = int(command[2])
        if car in cars:
            if cars[car]['miels'] - kilo < 10000:
                cars[car]['miels'] = 10000
            else:
                cars[car]['miels'] -= kilo
                print(f"{car} mileage decreased by {kilo} kilometers")
    command = input().split(" : ")

for car,info in sorted(cars.items(),key = lambda kvp: (-kvp[1]['miels'],kvp)):
    print(f"{car} -> Mileage: {info['miels']} kms, Fuel in the tank: {info['fuel']} lt.")