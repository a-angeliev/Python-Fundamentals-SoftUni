def sum_numvers(str):
    evens_sum = 0
    odds_sum = 0
    for el in str:
        el_as_int = int(el)
        if el_as_int % 2 == 0:
            evens_sum+=el_as_int
        else:
            odds_sum +=el_as_int
    print(f"Odd sum = {odds_sum}, Even sum = {evens_sum}")



stri =input()
sum_numvers(stri)
