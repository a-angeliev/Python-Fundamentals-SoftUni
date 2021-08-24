list = input().split()
lista=[]
listb=[]
listc=[]
a = int(len(list)/2)
num = int(input())
for i in range(num):
    for i in range(a):
        lista.append(list[i])
        listb.append(list[a+i])

    for b in range(a):
        listc.append(lista[b])
        listc.append(listb[b])
    list = listc
    listc=[]
    lista=[]
    listb=[]
print(list)

