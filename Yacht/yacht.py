# Score categories.
# Change the values as you see fit.
YACHT = 0
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = 7
FOUR_OF_A_KIND = 8
LITTLE_STRAIGHT = 9
BIG_STRAIGHT = 10
CHOICE = 11


def score(dice, category):
    dice.sort()
    if category == 0:
        if dice.count(dice[0]) == 5:
            return 50
        else:
            return 0
    if 0 < category < 7:
        return times_repeat(category, dice)
    if category == 7:
        if is_full_house(dice):
            return sum(dice)
        else:
            return 0
    if category == 8:
        return is_for_of_a_kind(dice)
    if category == 9:
        if dice == [1, 2, 3, 4, 5]:
            return 30
        else:
            return 0
    if category == 10:
        if dice == [2, 3, 4, 5, 6]:
            return 30
        else:
            return 0
    if category == 11:
        return sum(dice)


def times_repeat(number, dice):
    count = dice.count(number)
    return count * number


def is_full_house(dice):
    if dice.count(dice[0]) == 5:
        return False
    return dice.count(dice[0]) >= 2 and dice.count(dice[-1]) >= 2


def is_for_of_a_kind(dice):
    more_repeat = max(set(dice), key=dice.count)
    if dice.count(more_repeat) >= 4:
        return more_repeat * 4
    else:
        return 0
