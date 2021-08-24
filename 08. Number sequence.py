import sys
n = int(input())
max_num = 0
min_num = 0
for i in range(1,n+1):
    a = int(input())
    if a > max_num:
        max_num = a
    if a < min_num:
        min_num = a
print(f"Max number: {max_num}")
print(f"Min number: {min_num}")