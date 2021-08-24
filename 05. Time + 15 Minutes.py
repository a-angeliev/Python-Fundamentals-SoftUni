h = int(input())
m= int(input())
minutes = m+15
if minutes > 59:
    minutes = minutes % 60
    h = h+1
if h > 23:
    h = 0
if minutes <10:
    print(f'{h}:0{minutes}')
else:
    print(f"{h}:{minutes}")