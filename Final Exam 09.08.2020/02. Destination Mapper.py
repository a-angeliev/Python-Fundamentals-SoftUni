import re
pattern = r"(?P<sur>\=|/)(?P<destination>[A-Z][A-Za-z]{2,})(?P=sur)"

text = input()
destinations = []
start = 0
for match in re.finditer(pattern,text):
    destinations.append(match.group("destination"))
print(f"Destinations: ", end = "")
print(", ".join(destinations))
for el in destinations:
    start +=len(el)

print(f"Travel Points: {start}")