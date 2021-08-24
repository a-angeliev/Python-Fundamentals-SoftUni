stops = input()

command = input().split(":")
while not command[0] == "Travel":
    if command[0] == "Add Stop":
        index = int(command[1])
        string  = command[2]
        if 0<=index < len(stops):
            left_string = stops[:index]
            right_string = stops[index:]
            stops = left_string+string+right_string
        print(stops)

    if command[0] == "Remove Stop":
        start_index = int(command[1])
        end_index = int(command[2])
        if -len(stops)<=start_index<len(stops):
            if -len(stops)<=end_index<len(stops):

                left_string = stops[:start_index]
                right_string = stops[end_index+1:]
                stops = left_string+right_string
        print(stops)

    if command[0] == "Switch":
        old_string = command[1]
        new_string = command[2]
        if old_string in stops:
            stops = stops.replace(old_string,new_string)
        print(stops)
    command = input().split(":")

print(f"Ready for world tour! Planned stops: {stops}")

