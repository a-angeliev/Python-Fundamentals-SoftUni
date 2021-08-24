data = [el.strip() for el in input().split(", ")]
win1 = "$$$$$$"
win2 = "######"
win3 = "@@@@@@"
win4 = "^^^^^^"
win_char = ''
for el in data:
    if not len(el) == 20:
        print(f"invalid ticket")
    else:
        first_word = el[:10]
        second_word = el[10:]
        el = "\"" + el + "\""
        if win1 in first_word and win1 in second_word:
            win_char = "$"
        elif win2 in first_word and win2 in second_word:
            win_char = "#"
        elif win3 in first_word and win3 in second_word:
            win_char = "@"
        elif win4 in first_word and win4 in second_word:
            win_char = '^'
        else:
            print(f"ticket {el} - no match")

        win_rate = min(first_word.count(win_char),second_word.count(win_char))

        if win_rate<=9:
            print(f"ticket {el} - {win_rate}{win_char}")
        elif win_rate == 10:
            print(f"ticket {el} - {win_rate}{win_char} Jackpot!")