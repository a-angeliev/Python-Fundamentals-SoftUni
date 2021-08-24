text = input()
list= {}
for el in text:
    if not el == " ":
        if el not in list.keys():
            list[el] = 1
        else:
            list[el] +=1
for key,value in list.items():
    print(f"{key} -> {value}")