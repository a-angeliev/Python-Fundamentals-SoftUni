bar = ['.']*10

n = int(int(input())/10)
for i in range(n):
    bar[i] = '%'

if n*10<100:
    print(f"{n*10}% [{''.join(bar)}]")
    print(f"Still loading...")
else:
    print("100% Complete!")
    print(f"[{''.join(bar)}]")