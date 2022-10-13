import re


def is_armstrong_number(number):
    x = re.findall(r'\d', str(number))
    return number == sum([int(i) ** len(str(number)) for i in x])
