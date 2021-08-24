money = input().split(', ')
beggars = int(input())
list= []
k = 0
money = [int(x) for x in money]
for i in range(beggars):
    for m in range(i, len(money), beggars):
        k = k+ int(money[m])
    list.append(k)
    k=0
print(list)


