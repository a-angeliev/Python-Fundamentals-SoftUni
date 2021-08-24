n = int(input())
sum = 0
for i in range(1, int(n/2+1)):
    if n % i == 0:
        sum+=i

if sum == n:
    print("We have a perfect number!")
else:
    print('It\'s not so perfect.')
