n1 = int(input())
n2 = int(input())
oper = input()
if oper == '+':
    if (n1 +n2 ) %2 ==0:
        print(f"{n1} + {n2} = {n1+n2} - even")
    else:
        print(f"{n1} + {n2} = {n1 + n2} - odd")
elif oper == '-':
    if (n1 -n2 ) %2 ==0:
        print(f"{n1} - {n2} = {n1-n2} - even")
    else:
        print(f"{n1} - {n2} = {n1 - n2} - odd")
elif oper == '*':
    if (n1 * n2) % 2 == 0:
        print(f"{n1} * {n2} = {n1 * n2} - even")
    else:
        print(f"{n1} * {n2} = {n1 * n2} - odd")
elif oper == '/':
    if n2 !=0:
       print(f"{n1} / {n2} = {n1/n2:.2f}")
    else:
        print(f"Cannot divide {n1} by zero")
elif oper == '%':
    if n2 !=0:
        sum = n1 % n2
        print(f"{n1} % {n2} = {sum}")
    else:
        print(f"Cannot divide {n1} by zero")
