text = input()

data = input().split(":|:")
while not data[0] == "Reveal":
    if data[0] == 'InsertSpace':
        index = int(data[1])
        new_text = text[:index]+" "+text[index:]
        text = new_text
        print(text)
    if data[0] == "Reverse":
        substring = data[1]
        if substring in text:
            new_text = text.replace(substring,'',1)
            new_text+= substring[::-1]
            text = new_text
            print(text)
        else:
            print("error")

    if data[0] == "ChangeAll":
        substring = data[1]
        replacment = data[2]
        text = text.replace(substring,replacment)
        print(text)

    data = input().split(":|:")

print(f"You have a new text message: {text}")