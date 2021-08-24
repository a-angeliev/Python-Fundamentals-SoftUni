courses = {}
command = input().split(" : ")
while not command[0] == "end":
    if command[0] in courses.keys():
        courses[command[0]].append(command[1])
    else:
        courses[command[0]] = []
        courses[command[0]].append(command[1])
    command = input().split(" : ")

for courses,students in (sorted(courses.items(),key= lambda kvp: (-len(kvp[1])))):
    print(f"{courses}: {len(students)}")
    for student in sorted(students,key = lambda kvp:kvp):
        print(f"-- {student}")
