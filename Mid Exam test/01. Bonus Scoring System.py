import math
students_number = int(input())
lectures_sumber = int(input())
bonus = int(input())
a = 0
for _ in range(students_number):
    b = int(input())
    if b > a:
        a = b
if lectures_sumber == 0:
    print(f"Max Bonus: {0}.")
else:
    print(f"Max Bonus: {math.ceil(a / lectures_sumber * (5+bonus))}.")
print(f"The student has attended {a} lectures.")