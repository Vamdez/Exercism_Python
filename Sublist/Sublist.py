SUBLIST = 1
SUPERLIST = 2
EQUAL = 3
UNEQUAL = 0


def sublist(list_one, list_two):
    if list_one == list_two:
        return 3

    for i in range(len(list_one) - len(list_two) + 1):
        if not list_two or list_two == list_one[i: i + len(list_two)]:
            return 2

    for i in range(len(list_two) - len(list_one)+1):
        if not list_one or list_one == list_two[i: i + len(list_one)]:
            return 1
    return 0