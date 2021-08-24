bad_grades = int(input())
tasks_number = 0
bad_grades_count = 0
sum_grades = 0
avr = 0
while True:
    task = input()
    if task == 'Enough':
        print(f"Average score: {avrg:.2f}")
        print(f"Number of problems: {tasks_number}")
        print(f"Last problem: {last_task}")
        break
    last_task = task
    tasks_number +=1
    grade = int(input())
    sum_grades +=grade
    avrg= sum_grades/tasks_number
    if grade <=4:
        bad_grades_count+=1
    if bad_grades_count == bad_grades:
        print(f"You need a break, {bad_grades} poor grades.")
        break

