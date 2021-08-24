number_commands = int(input())
grades = {}
filtred_grades = {}
for _ in range(number_commands):
    name = input()
    grade = float(input())
    if name in grades.keys():
        grades[name].append(grade)
    else:
        grades[name] = []
        grades[name].append(grade)
for name,grade in grades.items():
    if sum(grade)/len(grade) >= 4.5:
        filtred_grades[name] = sum(grade)/len(grade)

for name,grade in sorted(filtred_grades.items(),key = lambda kvp: -kvp[1]):
    print(f"{name} -> {grade:.2f}")