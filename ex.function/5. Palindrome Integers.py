def palindromes_filter(list):
    for str in list:
        if str == str[::-1]:
            print("True")
        else:
            print("False")


numbers_list = input().split(", ")
palindromes_filter(numbers_list)
