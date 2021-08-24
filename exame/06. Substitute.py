k = int(input())
l = int(input())
m = int(input())
n = int(input())
a = 0

for i in range(k,9):
    for d in range(9,l-1,-1):
        for q in range(m,9):
            for z in range(9,n-1,-1):
                if i%2==0 and d%2==1 and q%2==0 and z%2==1:
                    if i!=q or  d!=z:
                        print(f"{i}{d} - {q}{z}")
                        a=a+1
                    else:
                        print(f"Cannot change the same player.")
                if a==6:
                    break
            if a == 6:
                break
        if a == 6:
            break
    if a == 6:
        break