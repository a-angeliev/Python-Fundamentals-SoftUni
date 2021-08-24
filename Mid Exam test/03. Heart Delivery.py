list = [int(x) for x in input().split('@')]
len = len(list) - 1
command = input()
step = 0
is_sucsees = True
count = 0
while not command == 'Love!':
    command = command.split()
    jump = int(command[1])
    step += jump
    if step > len:
        step = 0
    if not list[step]==0:
        list[step] -= 2
        if list[step] == 0:
            print(f"Place {step} has Valentine's day.")
    else:
        print(f"Place {step} already had Valentine's day.")

    command = input()
    if command == 'Love!':
        print(f"Cupid's last position was {step}.")
        for el in list:
            if not el ==0 :
                is_sucsees = False
                count +=1
        if is_sucsees:
            print("Mission was successful.")
        else:
            print(f"Cupid has failed {count} places.")