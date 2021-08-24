import re
data = input()
word = input()

pattern = rf"\b{word}\b"
list = []
for match in re.findall(pattern,data,flags = re.IGNORECASE):
    list.append(match)

print(len(list))