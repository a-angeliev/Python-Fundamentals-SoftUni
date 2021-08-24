email = input()
current_email = ''
command = input()
while not command == "Complete":
    command = command.split()
    if command[0] == "Make":
        if command[1] == "Upper":
            email = email.upper()
            print(email)

    if command[0] == "Make":
        if command[1] == "Lower":
            email = email.lower()
            print(email)

    if command[0] == "GetDomain":
        count  = int(command[1])
        print(email[-count:])

    if command[0] == "GetUsername":
        if "@" in email:
            for ch in email:
                if not ch == "@":
                    current_email+=ch
                else:
                    break
            print(current_email)
            current_email=""
        else:
            print(f"The email {email} doesn't contain the @ symbol.")

    if command[0] == "Replace":
        ch = command[1]
        email =email.replace(ch,"-")
        print(email)

    if command[0] == "Encrypt":
        for ch in email:
            print(ord(ch), end=" ")


    command = input()