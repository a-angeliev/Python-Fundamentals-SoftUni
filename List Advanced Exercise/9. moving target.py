def shoot(index,power,targets):
    if 0<=int(index)<=len(targets) - 1:
        targets[int(index)] -= int(power)
        if targets[int(index)]<= 0:
            targets.pop(int(index))
    return targets

def add(index, value, targets):
    if 0<=int(index) <= len(targets):
        targets.insert(int(index), int(value))

    else:
        print("Invalid placement!")
    return targets


def strike(index, radius,targets):
    if int(index) - int(radius) >=0 and int(index)+ int(radius) <= len(targets)-1:
        all_indexs = int(radius)*2 +1
        lowest_index = int(index) - int(radius)
        for _ in range(all_indexs):
            targets.pop(lowest_index)
    else:
        print("Strike missed!")
    return targets


targets = [int(x) for x in input().split()]
command = input()


while not command == 'End':
    new_command = command.split()

    if new_command[0] == 'Shoot':
        targets = shoot(new_command[1], new_command[2], targets)
    elif new_command[0] == 'Add':
        targets = add(new_command[1], new_command[2], targets)
    elif new_command[0] == 'Strike':
        targets = strike(new_command[1],new_command[2],targets)

    command = input()
    if command=='End':
        targets = [str(x) for x in targets]
        print(f"{'|'.join(targets)}")
