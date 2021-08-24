data =input()
unique = 0
new_string = ''
curent_sting = ''
for i in range(len(data)):
    if not data[i].isdigit():
        curent_sting+=data[i]
    else:
        if i < len(data)-1:
            if data[i+1].isdigit():
                ints = int(str(data[i])+str(data[i+1]))
            else:
                ints = data[i]
        else:
            ints = data[i]
        new_string +=curent_sting.upper() * int(ints)
        curent_sting = ''
print(f"Unique symbols used: {len(set(new_string))}")
print(new_string)
