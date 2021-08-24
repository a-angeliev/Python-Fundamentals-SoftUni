import sys
max_num = -sys.maxsize
sum_num = 0
n = int(input())
for i in range(0,n):
    a= int(input())
    if a >max_num:
        max_num =a
    sum_num = sum_num+a
if sum_num - max_num == max_num:
    print('Yes')
    print(f'Sum = {sum_num - max_num}')
else:
    print('No')
    print(f"Diff = {abs((sum_num -max_num) - max_num)}")