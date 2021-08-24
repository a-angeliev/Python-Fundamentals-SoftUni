dwarf_list ={}
data = input()
while not data == "Once upon a time":
    name,hat,physics = data.split(' <:> ')
    physics = int(physics)
    if not name in dwarf_list:
        dwarf_list[name] = {hat:physics}
    elif not hat in dwarf_list[name]:
        dwarf_list[name][hat] = physics
    else:
        if dwarf_list[name][hat] < physics:
            dwarf_list[name][hat] = physics
    data = input()
# sorted_dwarf  =dict(sorted(dwarf_list.items(), key = lambda kvp: (kvp[1])))
# for name,info in sorted(dwarf_list.items(), key = lambda kvp: (kvp[1]['physics'])):
#     for hat,physics in info.items():
#         print(f"({hat}) {name} <-> {physics}")
print(dwarf_list)
sorted_dwarf = dict(sorted(dwarf_list.items(),key = lambda kvp: (-sum(kvp[1].values(),kvp[1].most_common()))))
print(sorted_dwarf)