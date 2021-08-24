def exchange_by_index(numbers,index):
    first_digits = numbers[:index+1]
    second_digits = numbers[index+1:]
    result = second_digits+first_digits
    return result


def find_max_element(numbers, even_or_odd):
    list= []
    if even_or_odd == 'odd':
        for el in numbers:
            if not el % 2 == 0:
                list.append(el)
    else:
        for el in numbers:
            if el %2==0:
                list.append(el)

    if list == []:
        print("No matches")
        return

    max_number = max(list)
    for i in range(len(int_numbers)):
        if int_numbers[i] == max_number:
            result = i
    print(result)
    return


def find_min_element(numbers, even_or_odd):
    list = []
    if even_or_odd == 'odd':
        for el in numbers:
            if not el % 2 == 0:
                list.append(el)
    else:
        for el in numbers:
            if el % 2 == 0:
                list.append(el)

    if list == []:
        print("No matches")
        return

    max_number = min(list)
    for i in range(len(int_numbers)):
        if int_numbers[i] == max_number:
            result = i
    print(result)
    return


def find_first_numbers(numbers, count, even_or_odd):
    first_numbers = []
    if count > len(numbers):
        print('Invalid count')
        return
    if even_or_odd == 'odd':
        for el in numbers:
            if not el % 2 == 0:
                first_numbers.append(el)
            if len(first_numbers) == count:
                break
    else:
        for el in numbers:
            if el % 2 == 0:
                first_numbers.append(el)
            if len(first_numbers) == count:
                break
    print(first_numbers)
    return


def find_last_numbers(numbers, count, even_or_odd):
    last_numbers = []
    if count > len(numbers):
        print('Invalid count')
        return
    numbers = numbers[::-1]
    if even_or_odd == 'odd':
        for el in numbers:
            if not el % 2 == 0:
                last_numbers.append(el)
            if len(last_numbers) == count:
                break
    else:
        for el in numbers:
            if el % 2 == 0:
                last_numbers.append(el)
            if len(last_numbers) == count:
                break
    print(last_numbers[::-1])
    return





string_numbers = input().split()
int_numbers = [int(x) for x in string_numbers]
command_string = input()
if command_string == 'end':
    print(int_numbers)

while not command_string == "end":
    command_string = command_string.split()
    if command_string[0] == 'exchange':
        if 0<=int(command_string[1])< len(int_numbers):
            int_numbers = exchange_by_index(int_numbers, int(command_string[1]))
        else:
            print('Invalid index')

    if command_string[0] == 'max':
        find_max_element(int_numbers,command_string[1])

    if command_string[0] == 'min':
        find_min_element(int_numbers,command_string[1])

    if command_string[0] == 'first':
        find_first_numbers(int_numbers, int(command_string[1]), command_string[2])

    if command_string[0] == 'last':
        find_last_numbers(int_numbers, int(command_string[1]), command_string[2])

    command_string = input()
    if command_string=='end':
        print(int_numbers)