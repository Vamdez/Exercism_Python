import re


def is_valid(isbn):
    tot = 0
    multi = right_len = 10
    X_isdigit = False
    if isbn[-1] == 'X':
        X_isdigit = True
        isbn = isbn.replace('X', '10')
        right_len = 11
    formated = re.sub(r'\W', '', isbn)
    if not formated.isnumeric() or len(formated) != right_len:
        return False
    for val in formated:
        if multi == 1 and X_isdigit:
            tot += 10
            break
        tot += multi * int(val)
        multi -= 1
    return tot % 11 == 0
