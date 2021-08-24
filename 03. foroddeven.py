import sys
n = int(input())
oddsum = 0
oddmin = sys.maxsize
oddmax = -sys.maxsize
evensum = 0
evenmin = sys.maxsize
evenmax = -sys.maxsize
for i in range(0,n):
    a= float(input())
    if i%2 == 0:
        oddsum =oddsum +a
        if oddmax<a:
            oddmax = a
        if oddmin > a:
            oddmin = a
    else:
        evensum = evensum+a
        if evenmax <a:
            evenmax = a
        if evenmin >a:
            evenmin =a
print(f"OddSum={oddsum:.2f},")
if oddmin != sys.maxsize:
    print(f"OddMin={oddmin:.2f},")
else:
    print("OddMin=No,")
if oddmax != -sys.maxsize:
    print(f"OddMax={oddmax:.2f},")
else:
    print("OddMax=No,")
print(f"EvenSum={evensum:.2f},")
if evenmin != sys.maxsize:
    print(f"EvenMin={evenmin:.2f},")
else:
    print("EvenMin=No,")
if evenmax != -sys.maxsize:
    print(f"EvenMax={evenmax:.2f}")
else:
    print("EvenMax=No")