def sum_numbers(num1, num2):
    sum = num1+num2
    return sum

def subtract(result, num3):
    subtract = result-num3
    return subtract

def add_and_subtract(num1, num2, num3):
    sum = sum_numbers(num1, num2)
    subt = subtract(sum, num3)
    return subt

n1=int(input())
n2=int(input())
n3=int(input())
result = add_and_subtract(n1, n2, n3)
print(result)