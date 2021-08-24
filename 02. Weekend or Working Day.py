day = input()
if day == 'Sunday' or day == 'Saturday':
    print('Weekend')
elif day == 'Monday' or day == 'Tuesday' or day == 'Wednesday' or day == 'Thursday' or day == 'Friday':
    print('Working day')
else:
    print('Error')