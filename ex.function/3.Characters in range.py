def string_in_range(fchar,schar):
    first_int = ord(fchar)
    second_int = ord(schar)
    string = []
    for i in range(first_int+1, second_int):
        string.append(chr(i))
    print(' '.join(string))


a = input()
b = input()
string_in_range(a,b)