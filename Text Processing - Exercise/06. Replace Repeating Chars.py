data = input()
new_string = ''
current_letter = data[0]
for index in range(1,len(data)):
    if not current_letter == data[index]:
        new_string += current_letter
    current_letter = data[index]
if not new_string[:1:-1] == current_letter:
    new_string +=current_letter
print(new_string)