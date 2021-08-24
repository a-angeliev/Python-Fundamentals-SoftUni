list = input().split('#')
amount_of_water =  int(input())
effort = 0
total_fire = 0
cell = []
for fire in list:
    fire_info = fire.split(" = ")
    if  fire_info[0] == 'High' and  81<= int(fire_info[1])<= 125:
        if amount_of_water>= int(fire_info[1]):
            cell.append(int(fire_info[1]))
            amount_of_water -= int(fire_info[1])
            effort += 25/100 * int(fire_info[1])
            total_fire += int(fire_info[1])
    elif fire_info[0] == 'Medium' and 51 <= int(fire_info[1])<= 80:
        if amount_of_water>= int(fire_info[1]):
            cell.append(int(fire_info[1]))
            amount_of_water -= int(fire_info[1])
            effort += 25/100 * int(fire_info[1])
            total_fire += int(fire_info[1])
    elif fire_info[0] == 'Low' and 1 <= int(fire_info[1])<= 50:
        if amount_of_water>= int(fire_info[1]):
            cell.append(int(fire_info[1]))
            amount_of_water -= int(fire_info[1])
            effort += 25/100 * int(fire_info[1])
            total_fire += int(fire_info[1])
cell = [str(x) for x in cell]
print('Cells:')
for i in range(len(cell)):
    print(' -', cell[i])
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")