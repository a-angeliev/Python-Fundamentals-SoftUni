type = input()
r = int(input())
c = int(input())
if type == 'Premiere':
    print(f"{c*r*12:.2f} leva")
elif type =='Normal':
    print(f"{c * r * 7.5:.2f} leva")
elif type == 'Discount':
    print(f"{c * r * 5:.2f} leva")