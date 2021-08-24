data = input()
boomb_counter = 0
new_string = ''
for index in range(len(data)):
    if not data[index] == ">":
        if boomb_counter ==0:
            new_string+=data[index]
        else:
            boomb_counter-=1
    else:
        new_string+=data[index]
        boomb_counter +=int(data[index+1])

print(new_string)
