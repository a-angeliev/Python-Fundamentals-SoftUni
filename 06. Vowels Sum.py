string = input()
sum = 0
for char in string:
    if char == 'a':
        sum = sum+1
    elif char == 'e':
        sum = sum +2
    elif char =='i':
        sum= sum +3
    elif char == "o":
        sum = sum +4
    elif char == "u":
        sum = sum +5
print(sum)