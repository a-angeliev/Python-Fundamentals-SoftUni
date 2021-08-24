n = int(input())
suma= 0
sumb = 0
for i in range(1,n+1):
    a= int(input())
    if i%2==0:
        suma =suma +a
    else :
        sumb = sumb+a
if suma == sumb:
    print("Yes")
    print(f"Sum = {suma}")
else:
    print("No")
    print(f"Diff = {abs(suma-sumb)}")