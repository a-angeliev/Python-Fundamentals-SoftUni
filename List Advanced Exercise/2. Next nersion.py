version = input().split('.')
string = ''.join(version)
new_list= []
x = int(string)
x +=1
for el in str(x):
    new_list.append(el)
print(f"{'.'.join(new_list)}")

