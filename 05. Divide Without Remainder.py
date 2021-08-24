p1=0
p2=0
p3=0
n = int(input())
for i in range(0,n):
    a=int(input())
    if a%2==0:
        p1=p1+1
    if a%3 == 0:
        p2=p2+1
    if a%4 == 0:
        p3=p3+1
print(f"{p1/n*100:.2f}%")
print(f"{p2/n*100:.2f}%")
print(f"{p3/n*100:.2f}%")