import math
record = float(input())
distance = float(input())
time = float(input())

distancetime = distance * time
slow = (math.floor(distance/15) * 12.5)
ivanchotime = distancetime + slow
if ivanchotime < record:
    print(f"Yes, he succeeded! The new world record is {ivanchotime:.2f} seconds.")
else :
    print(f"No, he failed! He was {ivanchotime - record:.2f} seconds slower.")
