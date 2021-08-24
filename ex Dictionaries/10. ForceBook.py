def is_there_user(side_info:dict , force_user):
    for value in side_info.values():
        if force_user in value:
            return False
    return True
def is_there_user1(side_info:dict , force_user):
    for value in side_info.values():
        if force_user in value:
            return True
    return False
side_info = {}

command_line = input()
a=[]
flag = 0
is_user = False
if "|" in command_line:
    command_line = command_line.split(' | ')
    flag = 1
else:
    command_line = command_line.split(' -> ')
    flag = 2

while not command_line[0] == 'Lumpawaroo':

    if flag == 1:
        force_side = command_line[0]
        force_user = command_line[1]
        if not force_side in side_info.keys():
            if is_there_user(side_info,force_user):
                side_info[force_side] = []
                side_info[force_side].append(force_user)
        else:
            if is_there_user(side_info,force_user):
                side_info[force_side].append(force_user)
    elif flag == 2:
        force_side = command_line[1]
        force_user = command_line[0]
        if is_there_user1(side_info,force_user):
            if not force_side in side_info.keys():
                side_info[force_side] = []
            for keys,values in side_info.items():
                if force_user in values:
                    side_info[keys].remove(force_user)
                    break
            side_info[force_side].append(force_user)

        else:
            if force_side in side_info.keys():
                side_info[force_side].append(force_user)
            else:
                side_info[force_side] = []
                side_info[force_side].append(force_user)
        print(f"{force_user} joins the {force_side} side!")

    command_line = input()
    a = []
    flag = 0
    if "|" in command_line:
        command_line = command_line.split(' | ')
        flag = 1
    else:
        command_line = command_line.split(' -> ')
        flag = 2
for side,names in sorted(side_info.items(),key = lambda kvp: (-len(kvp[1]),kvp[0])):
    if not len(names) == 0:
        print(f"Side: {side}, Members: {len(names)}")
        for name in sorted(names, key=lambda kvp:kvp):
            print(f"! {name}")



