import re
pattern = r'(?P<sign>\:\:|\*\*)(?P<emoji>[A-Z][a-z]{2,})(?P=sign)'
tresh_pattern = r'\d'
data = input()
treshold = 1
emoji_numbers = 0
emojis =[]
current_tresh = 0
all_emoji = []
for match in re.findall(tresh_pattern,data):
    treshold *=int(match)
print(f"Cool threshold: {treshold}")

for match in re.finditer(pattern,data):
    emojis.append(match.group("emoji"))
    string_emoji = match.group("emoji")
    group = match.group("sign")
    current_emoji = group+string_emoji+group
    all_emoji.append(current_emoji)
    emoji_numbers+=1

print(f"{emoji_numbers} emojis found in the text. The cool ones are:")
index = 0
for el in emojis:
    for ch in el:
        current_tresh += ord(ch)
    if current_tresh>treshold:
        print(all_emoji[index])
        index +=1
    else:
        index +=1
    current_tresh = 0



