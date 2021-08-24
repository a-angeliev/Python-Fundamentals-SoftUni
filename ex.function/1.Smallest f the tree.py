def smallest_of_the_tree(num1, num2, num3):
    list= []
    list.append(num1)
    list.append(num2)
    list.append(num3)
    smallest = min(list)
    return smallest

first = int(input())
second = int(input())
tird = int(input())

result = smallest_of_the_tree(first,second,tird)
print(result)