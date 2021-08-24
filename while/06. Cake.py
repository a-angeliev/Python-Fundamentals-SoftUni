x= int(input())
y= int(input())
cake = x*y
pieces= 0

while pieces<=cake:
    a = input()
    if a =="STOP":
        break
    pieces += int(a)
if pieces <= cake:
    print(f"{cake-pieces} pieces are left.")
else:
    print(f"No more cake left! You need {pieces-cake} pieces more.")
