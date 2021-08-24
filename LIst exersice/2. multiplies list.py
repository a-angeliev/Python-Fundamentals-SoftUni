factor = int(input())
count = int(input())
m = 1
list= []
for i in range(count):
    while True:
        if m %factor== 0:
            list.append(m)
            m+=1
            break
        m += 1
print(list)