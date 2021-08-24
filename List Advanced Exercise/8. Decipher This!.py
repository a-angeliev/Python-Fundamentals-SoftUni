message = input().split()
count = 0
new_word = []
for el in message:
    for char in el:
        if char.isdigit():
            count +=1
    x = chr(int(el[:count]))
    last_elements = el[count:]
    new_word.append(x)
    for el in last_elements:
        new_word.append(el)
    new_word[1],new_word[-1] = new_word[-1], new_word[1]
    print(''.join(new_word), end =' ')
    new_word=[]
    count = 0