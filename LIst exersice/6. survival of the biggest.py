list = input().split()
list = [int(x) for x in list]
n = int(input())

for i in range(n):
    list.remove(min(list))
list = [str(x) for x in list]
print(', '.join(list))