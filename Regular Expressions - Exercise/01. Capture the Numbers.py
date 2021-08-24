import re

string = []
pattern  = r"\d+"

data = input()
while data:
    for match in re.finditer(pattern,data):
        string.append(match.group())



    data = input()
print(*string)