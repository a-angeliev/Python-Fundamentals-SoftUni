from collections import Counter
def rr(hat_numbers):
    a=[]
    for hat,numbers in sorted(hat_numbers.items(),key = lambda kvp: -kvp[1]):
        a.append(hat)
        return a

dwarf_list ={}
hat_numbers = {}
data = input()
while not data == "Once upon a time":
    flag = False
    name,hat,physics = data.split(' <:> ')
    physics = int(physics)
    if not name in dwarf_list:
        dwarf_list[name] = {hat:physics}
        flag = True
    elif not hat in dwarf_list[name]:
        dwarf_list[name][hat] = physics
        flag=True
    else:
        if dwarf_list[name][hat] < physics:
            dwarf_list[name][hat] = physics
    if flag:
        if hat in hat_numbers:
            hat_numbers[hat] +=1
        else:
            hat_numbers[hat] = 1
    data = input()

# sorted_dwarf  =dict(sorted(dwarf_list.items(), key = lambda kvp: (kvp[1])))
# for name,info in sorted(dwarf_list.items(), key = lambda kvp: (kvp[1]['physics'])):
#     for hat,physics in info.items():
#         print(f"({hat}) {name} <-> {physics}")
print(dwarf_list)
list = ['Red','Green','Blue']
sorted_dwarf = dict(sorted(dwarf_list.items(),key = lambda kvp: kvp[1]['Blue']))
for name,info in dwarf_list.items():
    for hat,physics in sorted(info.items(),key = lambda kvp: kvp['Blue']):
        print(f"({hat}) {name} <-> {physics}")

print(rr(hat_numbers))
print(hat_numbers)