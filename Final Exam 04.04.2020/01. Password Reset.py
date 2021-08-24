raw_password = input()
command = input().split()
new_password = ''
while not command[0] == "Done":
    if command[0] == "TakeOdd":
        for index in range(len(raw_password)):
            if index%2 == 1:
                new_password+= raw_password[index]
        raw_password = new_password
        new_password = ''
        print(raw_password)

    if command[0] == "Cut":
        start_index = int(command[1])
        lenght = int(command[2])
        end_index = start_index+lenght
        first_part = raw_password[:start_index]
        second_part = raw_password[end_index:]
        raw_password = first_part+second_part
        print(raw_password)

    if command[0] == "Substitute":
        substring = command[1]
        substitute = command[2]
        if substring in raw_password:
            list = raw_password.split(substring)
            new_password = substitute.join(list)
            raw_password = new_password
            new_password = ''
            print(raw_password)
        else:
            print("Nothing to replace!")
    command = input().split()
print(f"Your password is: {raw_password}")


