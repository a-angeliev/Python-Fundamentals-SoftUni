test = input()

data = input().split("|")
while not data[0] == "Decode":
    if data[0] == "Move":
        letter_numbers = int(data[1])

        first_letters = test[:letter_numbers]
        last_letters = test[letter_numbers:]
        test = last_letters+first_letters

    if data[0] == "Insert":
        index = int(data[1])
        value = data[2]

        if index<=len(test):
            first_part = test[:index]
            second_part = test[index:]
            test = first_part+value+second_part

    if data[0] == "ChangeAll":
        substring = data[1]
        replacement = data[2]
        if substring in test:
            test = test.replace(substring,replacement)

    data = input().split("|")

print(f"The decrypted message is: {test}")