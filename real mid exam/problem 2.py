list = input().split(" | ")
command = input().split()

while not command[0] == "Stop!":
    if command[0] == "Join":
        if not command[1] in list:
            list.append(command[1])
    elif command[0] == "Drop":
        if command[1] in list:
            list.remove(command[1])
    elif command[0] == "Replace":
        if command[1] in list and command[2] not in list:
            index = list.index(command[1])
            list[index] = command[2]
    command = input().split()
print(" ".join(list))