electrons  = int(input())
i = 1
atom = []
while electrons>0:
    if electrons > 2*i**2:
        atom.append(2*i**2)
        electrons-= 2*i**2
        i+=1
    else:
        atom.append(electrons)
        electrons=0

print(atom)
