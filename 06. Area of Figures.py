import  math
shape = str(input())
if shape == 'square':
    a = float(input())
    print(f"{a*a:.3f}")
elif shape == 'rectangle':
    a = float(input())
    b = float(input())
    print(f"{a*b:.3f}")
elif shape == 'circle':
    r = float(input())
    print(f"{r*r*math.pi:.3f}")
elif shape == 'triangle':
    a = float(input())
    h = float(input())
    print(f"{a * h / 2:.3f}")