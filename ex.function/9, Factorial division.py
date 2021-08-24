first_number = int(input())
second_number = int(input())

first_factorial =1
second_factorial = 1
for i in range(1,first_number+1):
    first_factorial *= i

for m in range(1, second_number+1):
    second_factorial*=m

print(f"{first_factorial/second_factorial:.2f}")
