numbers = [int(x) for x in input().split(', ')]
positive = []
negative = []
even = []
odd = []
for el in numbers:
    if el >= 0:
        positive.append(str(el))
    else:
        negative.append(str(el))

    if el % 2 == 0:
        even.append(str(el))
    else:
        odd.append(str(el))

print(f"Positive: {', '.join(positive)}")
print(f"Negative: {', '.join(negative)}")
print(f"Even: {', '.join(even)}")
print(f"Odd: {', '.join(odd)}")
