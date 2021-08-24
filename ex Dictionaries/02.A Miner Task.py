list = {}
new_list = []
line = input()
while not line =='stop':
    new_list.append(line)
    line = input()

for index in range(0, len(new_list), 2):
    if new_list[index] not in list:
        list[new_list[index]] = int(new_list[index+1])
    else:
        list[new_list[index]] += int(new_list[index+1])


for key,value in list.items():
    print(f"{key} -> {value}")