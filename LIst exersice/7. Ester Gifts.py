gifts = input().split()
commands = input()
o=0
if commands != 'No Money':
    commands = commands.split()

while commands!= 'No Money':
    if commands[0] == 'OutOfStock':
        for i in range(len(gifts)):
            if commands[1] == gifts[i]:
                gifts[i] = None
    if commands[0] == 'Required' and 0<=int(commands[2]) < len(gifts):
        gifts[int(commands[2])] = commands[1]
    if commands[0] == 'JustInCase':
        gifts[len(gifts)-1] = commands[1]
    commands = input()
    if commands != 'No Money':
        commands = commands.split()
for m in range(len(gifts)):
    if gifts[m] == None:
        o +=1
for k in range(o):
    gifts.remove(None)
print(' '.join(gifts))


