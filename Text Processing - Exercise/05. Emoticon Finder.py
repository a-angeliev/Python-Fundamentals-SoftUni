data = input()

for index in range(len(data)):
    if data[index] == ":":
        print(data[index] + data[index+1])