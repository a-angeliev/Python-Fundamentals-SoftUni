import re
string = []
data = input()
pattern = r"\b\_(?P<ss>[A-Za-z0-9]+)\b"
for match in re.finditer(pattern,data):
    string.append(match.group("ss"))

print(','.join(string))