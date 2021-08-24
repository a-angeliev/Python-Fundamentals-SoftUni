n = int(input())
suma= 0
sumb= 0
for i in range(0,n):
    a= int(input())
    suma= suma+a
for i in range(0,n):
    b = int(input())
    sumb = sumb+b

if suma ==sumb:
    print(f"Yes, sum = {suma} ")
else:
    print(f"No, diff = {abs(suma - sumb)}")
