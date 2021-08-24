import re
pattern = r"(\s(?P<email>[A-Za-z]+[A-Za-z\.\-\_]*[A-Za-z]+\@[A-Za-z]+[A-Za-z\-]*[A-Za-z]+(\.[A-Za-z]+[A-Za-z\-]*[A-Za-z]+)+))\b"
data = input()

for match in re.finditer(pattern,data):
    print(match.group('email'))