import re
pattern = r"(?P<url>www\.[A-Za-z0-9]+[A-Za-z0-9\-]+\.[a-z]+(\.[a-z]+)*)"

data = input()
while data:
    for match in re.finditer(pattern, data):
        print(match.group('url'))

    data = input()