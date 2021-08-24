def is_password_valid(password):
    is_valid = True
    digits = 0
    sum_digits = 0
    password_check = str(password)
    if not 6<= len(password)<=10:
        print("Password must be between 6 and 10 characters")
        is_valid = False

    if not password.isalnum():
        print("Password must consist only of letters and digits")
        is_valid = False


    for el in password:
        if el.isdigit():
            digits +=1
        if digits == 2:
            break
    if digits < 2:
        print("Password must have at least 2 digits")
        is_valid = False

    if is_valid:
        print("Password is valid")

pas = input()
is_password_valid(pas)