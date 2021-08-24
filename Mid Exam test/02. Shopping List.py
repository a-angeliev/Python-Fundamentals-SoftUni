list = [x for x in input().split('!')]
command = input()

while not command == 'Go Shopping!':
    command = command.split()
    if command[0] == 'Urgent':
        if not command[1] in list:
            list.insert(0,command[1])
    if command[0] == 'Unnecessary':
        if command[1] in list:
           list.remove(command[1])
    if command[0] == 'Correct':
        if command[1] in list:
            index = list.index(command[1])
            list[index] = command[2]
    if command[0] == 'Rearrange':
        if command[1] in list:
            list.remove(command[1])
            list.append(command[1])
    command = input()
print(f"{', '.join(list)}")