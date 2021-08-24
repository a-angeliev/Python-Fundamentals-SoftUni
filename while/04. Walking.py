all_steps = 0
going_home = False
while all_steps<10000:
    steps = input()
    if steps == 'Going home':
        steps = input()
        all_steps +=int(steps)
        going_home = True
        break
    all_steps += int(steps)
if all_steps<10000:
    print(f"{10000 - all_steps} more steps to reach goal.")
else:
    print(f"Goal reached! Good job!")
    print(f"{all_steps - 10000} steps over the goal!")


