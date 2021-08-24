def validation(courses_info, courses,password):
    if courses in courses_info:
        if courses_info[courses] == password:
            return True
    return False

def add_info_for_student(results:dict, contest,username,points):
    if not username in results:
        results[username] = {contest:points}
    elif not contest in results[username]:
        results[username][contest] = points

    else:
        if results[username][contest] < points:
            results[username][contest] = points

def best_candidate(results):
    name = None
    pointss = 0
    for namea,info in results.items():
        c_points=0
        for course,points in info.items():
            c_points +=points
        if pointss <c_points:
            pointss = c_points
            name = namea

    print(f"Best candidate is {name} with total {pointss} points.")
    print("Ranking:")

def print_all_users(results):
    for username,info in sorted(results.items()):
        print(f'{username}')
        for cours,points in sorted(info.items(),key = lambda kvp: (-kvp[1],kvp[0])):
            print(f"#  {cours} -> {points} ")


courses_info = {}
data = input()
results = {}

while not data == "end of contests":
    course,password = data.split(":")
    courses_info[course] = password
    data = input()

data = input()
while not data == "end of submissions":
    contest,password,username,points = data.split("=>")
    points = int(points)
    if validation(courses_info,contest,password):
        add_info_for_student(results,contest,username,points)
    data = input()

best_candidate(results)
print_all_users(results)