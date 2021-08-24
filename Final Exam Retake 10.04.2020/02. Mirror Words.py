import re
pattern = r'(?P<sur>\@|\#)(?P<fw>[A-Za-z]{3,})(?P=sur){2}(?P<sw>[A-Za-z]{3,})(?P=sur)'

text = input()
mirror_words = []
founded = 0
for match in re.finditer(pattern,text):
    founded +=1
    fw = match.group('fw')
    sw = match.group('sw')
    if fw == sw[::-1]:
        mirror_words.append(fw)

if founded == 0:
    print("No word pairs found!")
else:
    print(f"{founded} word pairs found!")

if not mirror_words == []:
    print("The mirror words are:")
    for index in range(len(mirror_words)):
        el = mirror_words[index]
        if not index == len(mirror_words)-1:
            print(f"{el} <=> {el[::-1]}" , end =", ")
        else:
            print(f"{el} <=> {el[::-1]}")
else:
    print("No mirror words!")

