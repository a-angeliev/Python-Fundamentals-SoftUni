import re
lines_number = int(input())
pattern = r"^\@\#+[A-Z][A-Za-z0-9]{4,}[A-Z]\@\#+$"
new_pattern = r"\d"
group = ""
current_mathc = None
for _ in range(lines_number):
    data = input()
    for match in re.finditer(pattern,data):
        current_mathc = match.group()

    if not current_mathc == None:
        for match in re.finditer(new_pattern,current_mathc):
          group +=match.group()
        if group == '':
            group = "00"
        print(f"Product group: {group}")
        group = ''
        current_mathc = None

    else:
        print("Invalid barcode")