raw_key = input()
command = input()
new_string = ''
while not command == 'Generate':
    command = command.split(">>>")
    if command[0] == "Contains":
        substring = command[1]
        if substring in raw_key:
            print(f"{raw_key} contains {substring}")
        else:
            print("Substring not found!")


    elif command[0] =='Flip':
        up_low = command[1]
        start_index =int(command[2])
        end_index = int(command[3])
        if up_low == "Upper":
            first_part = raw_key[:start_index]
            secound_part = raw_key[end_index:]
            for i in range(start_index,end_index):
                new_string += raw_key[i].upper()
            raw_key = first_part+new_string+secound_part
            new_string = ""
            print(raw_key)
        elif up_low =="Lower":
            first_part = raw_key[:start_index]
            secound_part = raw_key[end_index:]
            for i in range(start_index, end_index):
                new_string += raw_key[i].lower()
            raw_key = first_part + new_string + secound_part
            new_string = ""
            print(raw_key)

    elif command[0] =='Slice':
        start_index = int(command[1])
        end_index = int(command[2])
        first_part = raw_key[:start_index]
        secound_part_part = raw_key[end_index:]
        raw_key = first_part+secound_part_part
        print(raw_key)


    command = input()
print(f"Your activation key is: {raw_key}")