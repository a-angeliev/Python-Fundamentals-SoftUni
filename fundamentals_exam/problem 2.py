import re
pattern = r"^(?P<sur>\$|\%)(?P<mes>[A-Z][a-z]{2,})(?P=sur): (?P<dig>\[\d+\]\|\[\d+\]\|\[\d+\]\|)$"

number_of_inputs = int(input())
list = []
cur_char = ''
tag = ''
for _ in range(number_of_inputs):
    data = input()
    for match in re.finditer(pattern,data):
        tag = match.group("mes")
        a = match.group("dig")
    if not tag == '':

        for ch in a:
            if ch.isdigit():
                cur_char +=ch
            else:
                cur_char+=" "
        list = cur_char.split()
        cur_char = ''

        for index in range(len(list)):
            list[index] = int(list[index])
        print(f"{tag}: {chr(list[0])}{chr(list[1])}{chr(list[2])}")
        list = []
        tag = ''
    else:
        print(f"Valid message not found!")
