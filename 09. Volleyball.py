from math import floor
year =  input()
holydays = int(input())
selo_weekends = int(input())
sofia_weekends = (48 - selo_weekends) * 3/4
sofia_weekends_p = sofia_weekends
holydays_p = holydays* 2/3
if year == "leap":
    all_game = (sofia_weekends_p + holydays_p+selo_weekends)*115/100
else:
    all_game = sofia_weekends_p+holydays_p+selo_weekends
print(floor(all_game))