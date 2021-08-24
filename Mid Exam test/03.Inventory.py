list = input().split(', ')
command = input()
while not command == "Craft!":
    comma, item = command.split(' - ')
    if comma == 'Collect':
        if not item in list:
            list.append(item)

    if comma == 'Drop':
        if item in list:
            list.remove(item)

    if comma == 'Combine Items':
        old_item, new_item = item.split(':')
        if old_item in list:
            index_old_item = list.index(old_item)
            list.insert(index_old_item+1, new_item)
    if comma == 'Renew':
        if item in list:
            list.remove(item)
            list.append(item)

    command = input()
    if command =="Craft!":
        print(f"{', '.join(list)}")