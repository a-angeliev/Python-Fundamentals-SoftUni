data = input().split(", ")
flag = True
for i in range(len(data)):
    current_username = data[i]
    if 3<= len(current_username)<= 16:
        for i in current_username:
            if not i.isdigit():
                if not i.isalpha():
                    if not i == '-':
                        if not i =="_":
                            flag = False
                            break
        if flag:
            print(current_username)
        flag = True

