first_string = input()
second_string = input()
print_string = first_string
last_string = ''
for i in range(len(first_string)):
    print_string = print_string.replace(first_string[i], second_string[i],1)
    if not last_string == print_string:
        print(print_string)
    last_string = print_string