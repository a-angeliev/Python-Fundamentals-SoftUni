first_line = input().split(', ')
second_line = input().split(", ")
new_list=[]
for el in first_line:
    for ell in second_line:
        if el in ell:
            new_list.append(el)

print(sorted(set(new_list), key =first_line.index))
