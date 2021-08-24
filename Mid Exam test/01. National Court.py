import math
final_time = 0
first_emp = int(input())
second_emp = int(input())
trd_emp = int(input())
pph = first_emp+second_emp+trd_emp
all_ppl = int(input())
needed_time = all_ppl/pph
while not needed_time == 0:
    if needed_time <= 3:
        final_time+= needed_time
        needed_time= 0
    else:
        needed_time -= 3
        final_time +=4
final_time = math.ceil(final_time)
print(f"Time needed: {int(final_time)}h.")
