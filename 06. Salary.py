n=int(input())
salary = int(input())
fine = 0
for i in range(0,n):
    name = input()
    if name =="Facebook":
        fine = fine + 150
    elif name == "Instagram":
        fine = fine +100
    elif name == "Reddit":
        fine = fine +50

    if fine >= salary:
        print("You have lost your salary.")
        break




if salary-fine>0:
    print(salary - fine)